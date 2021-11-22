# https://realpython.com/python-gil/

# Single threaded count. Takes around 38s.

import time
from threading import Thread

count = 900000000

def countdown(n):
    while n>0:
        n -= 1    

start = time.time()
countdown(count)
end = time.time()

print('Time taken to process: ', end - start)

