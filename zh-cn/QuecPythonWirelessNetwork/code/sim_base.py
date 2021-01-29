# 参考文档
# https://python.quectel.com/wiki/#/zh-cn/api/?id=sim-sim%e5%8d%a1
import sim
import utime as time
import urandom as random
# 打印所有通讯录


def print_sim_phonebook():
    for i in range(1, 1000):
        # 一次读一个
        info = sim.readPhonebook(9, i, i+1, "")
        if info == -1:
            print("read has error")
            break
        else:
            print(info)
            time.sleep_ms(5)

# 生成随机名字


def CreatRandomStr(length):
    # The limit for the extended ASCII Character set
    MAX_LENGTH = 16
    random_string = ''
    if length > MAX_LENGTH:
        length = length % MAX_LENGTH
    if length == 0:
        length = random.randint(1, MAX_LENGTH)
    for _ in range(length):
        # 0 ~ z
        random_integer = random.randint(48, 122)
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return random_string


def CreatRandomPhoneNum(count=8):
    pre_lst = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150",
               "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    # 生成8个随机数个位数
    tail_str = [str(random.randint(0, 9)) for i in range(count)]
    # 将其转化为字符串
    tail_str = ''.join(tail_str)
    return random.choice(pre_lst) + tail_str
    pass


def write_random_sim_phonebook():
    for i in range(1, 10):
        # 一次写一个
        name = CreatRandomStr(random.randint(4, 6))
        number = CreatRandomPhoneNum()
        sim.writePhonebook(9, i, name, number)


def test_sim_base():
    # check sim statsu
    ret = sim.getStatus()
    if ret == 1:
        write_random_sim_phonebook()
        print_sim_phonebook()
    else:
        # 状态不对
        print("sim status has error , value is {0}".format(ret))
    print("test_sim_base has exited")


if __name__ == "__main__":
    test_sim_base()
