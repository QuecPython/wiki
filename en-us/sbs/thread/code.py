import _thread

def th_func(thread_id):
	print("thread id is:%d" % thread_id)

for i in range(5):
	_thread.start_new_thread(th_func,(i+1,))