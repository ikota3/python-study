import threading
import time


def run(n):
    print(f"Thread {n}")
    time.sleep(3)


for i in range(3):
    threading.Thread(target=run, args=(i,)).start()

print('Create three threads')
print(threading.active_count())

"""Output
>> Thread 0
>> Thread 1
>> Thread 2
>> Create three threads
>> 4
"""
