import sys
import time
import os


try:
	stdout = sys.stdout.buffer
except AttributeError:
	# Python2 doesn't have buffer attr
	stdout = sys.stdout


def stdout_write_bytes(b):
	b = b.replace(b"\x04", b"")
	stdout.write(b)
	stdout.flush()

class QuecpythonError(Exception):
	pass
	
	
class Quecpython:
	def __init__(self, device, baudrate=115200, wait=0):
		import serial
		delayed = False
		for attempt in range(wait + 1):
			try:
				self.serial = serial.Serial(device, baudrate=baudrate, interCharTimeout=1)
				break
			except (OSError, IOError):  # Py2 and Py3 have different errors
				if wait == 0:
					continue
				if attempt == 0:
					sys.stdout.write("Waiting {} seconds for Quecpython ".format(wait))
					delayed = True
			time.sleep(1)
			sys.stdout.write(".")
			sys.stdout.flush()
		else:
			if delayed:
				print("")
			raise QuecpythonError("failed to access " + device)
		if delayed:
			print("")
			
	def close(self):
		self.serial.close()

	def read_until(self, min_num_bytes, ending, timeout=10, data_consumer=None):
		# if data_consumer is used then data is not accumulated and the ending must be 1 byte long
		assert data_consumer is None or len(ending) == 1

		data = self.serial.read(min_num_bytes)
		if data_consumer:
			data_consumer(data)
		timeout_count = 0
		while True:
			if data.endswith(ending):
				break
			elif self.serial.inWaiting() > 0:
				new_data = self.serial.read(1)
				if data_consumer:
					data_consumer(new_data)
					data = new_data
				else:
					data = data + new_data
				timeout_count = 0
			else:
				timeout_count += 1
				if timeout is not None and timeout_count >= 100 * timeout:
					break
				time.sleep(0.01)
		return data
		
	def enter_raw_repl(self):
		self.serial.write(b"\r\x03\x03")  # ctrl-C twice: interrupt any running program

		# flush input (without relying on serial.flushInput())
		n = self.serial.inWaiting()
		while n > 0:
			self.serial.read(n)
			n = self.serial.inWaiting()

		self.serial.write(b"\r\x01")  # ctrl-A: enter raw REPL
		data = self.read_until(1, b"raw REPL; CTRL-B to exit\r\n>")
		if not data.endswith(b"raw REPL; CTRL-B to exit\r\n>"):
			print(data)
			raise QuecpythonError("could not enter raw repl")

		self.serial.write(b"\x04")  # ctrl-D: soft reset
		data = self.read_until(1, b"soft reboot\r\n")
		if not data.endswith(b"soft reboot\r\n"):
			print(data)
			raise QuecpythonError("could not enter raw repl")
		# By splitting this into 2 reads, it allows boot.py to print stuff,
		# which will show up after the soft reboot and before the raw REPL.
		data = self.read_until(1, b"raw REPL; CTRL-B to exit\r\n")
		if not data.endswith(b"raw REPL; CTRL-B to exit\r\n"):
			print(data)
			raise QuecpythonError("could not enter raw repl")
	def exit_raw_repl(self):
		self.serial.write(b"\r\x02")  # ctrl-B: enter friendly REPL
		
	def follow(self, timeout, data_consumer=None):
		# wait for normal output
		data = self.read_until(1, b"\x04", timeout=timeout, data_consumer=data_consumer)
		if not data.endswith(b"\x04"):
			raise QuecpythonError("timeout waiting for first EOF reception")
		data = data[:-1]

		# wait for error output
		data_err = self.read_until(1, b"\x04", timeout=timeout)
		if not data_err.endswith(b"\x04"):
			raise QuecpythonError("timeout waiting for second EOF reception")
		data_err = data_err[:-1]

		# return normal and error output
		return data, data_err

	def exec_raw_no_follow(self, command):
		if isinstance(command, bytes):
			command_bytes = command
		else:
			command_bytes = bytes(command, encoding="utf8")

		# check we have a prompt
		data = self.read_until(1, b">")
		if not data.endswith(b">"):
			raise QuecpythonError("could not enter raw repl")

		# write command
		for i in range(0, len(command_bytes), 256):
			self.serial.write(command_bytes[i : min(i + 256, len(command_bytes))])
			time.sleep(0.1)
		self.serial.write(b"\x04")

		# check if we could exec command
		data = self.serial.read(2)
		if data != b"OK":
			raise QuecpythonError("could not exec command (response: %r)" % data)

	def exec_raw(self, command, timeout=10, data_consumer=None):
		self.exec_raw_no_follow(command)
		return self.follow(timeout, data_consumer)

	def eval(self, expression):
		ret = self.exec_("print({})".format(expression))
		ret = ret.strip()
		return ret

	def exec_(self, command, data_consumer=None):
		ret, ret_err = self.exec_raw(command, data_consumer=data_consumer)
		if ret_err:
			raise QuecpythonError("exception", ret, ret_err)
		return ret

	def execfile(self, filename):
		with open(filename, "rb") as f:
			pyfile = f.read()
			print(pyfile)
		return self.exec_(pyfile)
	def fs_ls(self, src):
		cmd = (
			"import uos\nfor f in uos.ilistdir(%s):\n"
			" print('{:12} {}{}'.format(f[3]if len(f)>3 else 0,f[0],'/'if f[1]&0x4000 else ''))"
			% (("'%s'" % src) if src else "")
		)
		self.exec_(cmd, data_consumer=stdout_write_bytes)

	def fs_cat(self, src, chunk_size=256):
		cmd = (
			"with open('%s') as f:\n while 1:\n"
			"  b=f.read(%u)\n  if not b:break\n  print(b,end='')" % (src, chunk_size)
		)
		self.exec_(cmd, data_consumer=stdout_write_bytes)

	def fs_get(self, src, dest, chunk_size=256):
		self.exec_("f=open('%s','rb')\nr=f.read" % src)
		with open(dest, "wb") as f:
			while True:
				data = bytearray()
				self.exec_("print(r(%u))" % chunk_size, data_consumer=lambda d: data.extend(d))
				assert data.endswith(b"\r\n\x04")
				data = eval(str(data[:-3], "ascii"))
				if not data:
					break
				f.write(data)
		self.exec_("f.close()")

	def fs_put(self, src, dest, chunk_size=256):
		self.exec_("f=open('%s','wb')\nw=f.write" % dest)
		with open(src, "rb") as f:
			while True:
				data = f.read(chunk_size)
				if not data:
					break
				if sys.version_info < (3,):
					self.exec_("w(b" + repr(data) + ")")
				else:
					self.exec_("w(" + repr(data) + ")")
		self.exec_("f.close()")

	def fs_mkdir(self, dir):
		self.exec_("import uos\nuos.mkdir('%s')" % dir)

	def fs_rmdir(self, dir):
		self.exec_("import uos\nuos.rmdir('%s')" % dir)

	def fs_rm(self, src):
		self.exec_("import uos\nuos.remove('%s')" % src)

setattr(Quecpython, "exec", Quecpython.exec_)

def execfile(filename, device="COM24", baudrate=115200):
	qpy = Quecpython(device, baudrate)
	qpy.enter_raw_repl()
	output = qpy.execfile(filename)
	stdout_write_bytes(output)
	qpy.exit_raw_repl()
	qpy.close()

def filesystem_command(qpy, args):
	def fname_remote(src):
		if src.startswith(":"):
			src = src[1:]
		return src

	def fname_cp_dest(src, dest):
		src = src.rsplit("/", 1)[-1]
		if dest is None or dest == "":
			dest = src
		elif dest == ".":
			dest = "./" + src
		elif dest.endswith("/"):
			dest += src
		return dest

	cmd = args[0]
	args = args[1:]
	try:
		if cmd == "cp":
			srcs = args[:-1]
			dest = args[-1]
			if srcs[0].startswith("./") or dest.startswith(":"):
				op = qpy.fs_put
				fmt = "cp %s :%s"
				dest = fname_remote(dest)
			else:
				op = qpy.fs_get
				fmt = "cp :%s %s"
			for src in srcs:
				src = fname_remote(src)
				dest2 = fname_cp_dest(src, dest)
				print(fmt % (src, dest2))
				op(src, dest2)
		else:
			op = {
				"ls": qpy.fs_ls,
				"cat": qpy.fs_cat,
				"mkdir": qpy.fs_mkdir,
				"rmdir": qpy.fs_rmdir,
				"rm": qpy.fs_rm,
			}[cmd]
			if cmd == "ls" and not args:
				args = [""]
			for src in args:
				src = fname_remote(src)
				print("%s :%s" % (cmd, src))
				op(src)
	except QuecpythonError as er:
		print(str(er.args[2], "ascii"))
		qpy.exit_raw_repl()
		qpy.close()
		sys.exit(1)

def main():
	import argparse
	cmd_parser = argparse.ArgumentParser(description="Run scripts on the EC100Y.")
	cmd_parser.add_argument(
		"-d",
		"--device",
		default=os.environ.get("EC100Y_DEVICE", "COM24"),
		help="the serial device of the EC100Y",
	)
	cmd_parser.add_argument(
		"-b",
		"--baudrate",
		default=os.environ.get("EC100Y_BAUDRATE", "115200"),
		help="the baud rate of the serial device",
	)
	cmd_parser.add_argument("-c", "--command", help="program passed in as string")
	cmd_parser.add_argument(
		"-w",
		"--wait",
		default=0,
		type=int,
		help="seconds to wait for USB connected board to become available",
	)
	group = cmd_parser.add_mutually_exclusive_group()
	group.add_argument(
		"--follow",
		action="store_true",
		help="follow the output after running the scripts [default if no scripts given]",
	)
	group.add_argument(
		"--no-follow",
		action="store_true",
		help="Do not follow the output after running the scripts.",
	)
	cmd_parser.add_argument(
		"-f", "--filesystem", action="store_true", help="perform a filesystem action"
	)
	cmd_parser.add_argument("files", nargs="*", help="input files")
	args = cmd_parser.parse_args()
	# open the connection to the qpyoard
	try:
		qpy = Quecpython(args.device, args.baudrate, args.wait)
	except QuecpythonError as er:
		print(er)
		sys.exit(1)

	# run any command or file(s)
	if args.command is not None or args.filesystem or len(args.files):
		# we must enter raw-REPL mode to execute commands
		# this will do a soft-reset of the board
		try:
			qpy.enter_raw_repl()
		except QuecpythonError as er:
			print(er)
			qpy.close()
			sys.exit(1)

		def execbuffer(buf):
			try:
				if args.no_follow:
					qpy.exec_raw_no_follow(buf)
					ret_err = None
				else:
					ret, ret_err = qpy.exec_raw(
						buf, timeout=None, data_consumer=stdout_write_bytes
					)
			except QuecpythonError as er:
				print(er)
				qpy.close()
				sys.exit(1)
			except KeyboardInterrupt:
				sys.exit(1)
			if ret_err:
				qpy.exit_raw_repl()
				qpy.close()
				stdout_write_bytes(ret_err)
				sys.exit(1)

		# do filesystem commands, if given
		if args.filesystem:
			filesystem_command(qpy, args.files)
			del args.files[:]

		# run the command, if given
		if args.command is not None:
			execbuffer(args.command.encode("utf-8"))

		# run any files
		for filename in args.files:
			with open(filename, "rb") as f:
				pyfile = f.read()
				execbuffer(pyfile)

		# exiting raw-REPL just drops to friendly-REPL mode
		qpy.exit_raw_repl()

	# if asked explicitly, or no files given, then follow the output
	if args.follow or (args.command is None and not args.filesystem and len(args.files) == 0):
		try:
			ret, ret_err = qpy.follow(timeout=None, data_consumer=stdout_write_bytes)
		except QuecpythonError as er:
			print(er)
			sys.exit(1)
		except KeyboardInterrupt:
			sys.exit(1)
		if ret_err:
			qpy.close()
			stdout_write_bytes(ret_err)
			sys.exit(1)

	# close the connection to the EC100Y
	qpy.close()


if __name__ == "__main__":
	main()