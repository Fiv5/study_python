import time
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for _ in range(100000):
        # 获取锁:
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


start = time.time()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(balance)
print('共耗时 %.2f s' % (end - start))
