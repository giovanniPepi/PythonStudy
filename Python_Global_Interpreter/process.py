# Instead of 2 threads, this creates 2 process and will run faster because it's not limited by GIL

from multiprocessing import Pool
import time

count = 900000000

def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [count//2])
    r2 = pool.apply_async(countdown, [count//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time(s) taken to process: ', end - start)

