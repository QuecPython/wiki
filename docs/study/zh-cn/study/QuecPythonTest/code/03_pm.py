# 实验1：	待机唤醒实验
# API资料参考连接：
# https://python.quectel.com/wiki/#/zh-cn/api/?id=pm-%e4%bd%8e%e5%8a%9f%e8%80%97

import pm
import utime


def main():
    lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))  # 创建wake_lock锁
    pm.autosleep(1)  # 自动休眠模式控制

    while True:
        print("sleep")
        utime.sleep(5)  # 延时 并 休眠5秒钟
        res = pm.wakelock_lock(lpm_fd)  # 加锁 禁止进入休眠状态
        print(res)
        print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" % lpm_fd)
        print("not sleep")
        utime.sleep(5)  # 只延时，不休眠
        res = pm.wakelock_unlock(lpm_fd)  # 解锁 继续 自动休眠模式
        print(res)
        print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
        num = pm.get_wakelock_num()  # 获取已创建锁的数量
        print(num)  # 打印已创建锁的数量


if __name__ == "__main__":
    main()
