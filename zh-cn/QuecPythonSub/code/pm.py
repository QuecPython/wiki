import pm
import utime

lpm_fd = pm.create_wakelock("test_lock", len("test_lock"))
pm.autosleep(1)

while 1:
    print("sleep")
    utime.sleep(5)
    res = pm.wakelock_lock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_lock, g_c1_axi_fd = %d" %lpm_fd)
    print("not sleep")
    utime.sleep(5)
    res = pm.wakelock_unlock(lpm_fd)
    print(res)
    print("ql_lpm_idlelock_unlock, g_c1_axi_fd = %d" % lpm_fd)
    num = pm.get_wakelock_num()
    print(num)
    