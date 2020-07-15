import threading
import time


def run(arg):
    print(f"arg: {arg}, thread name: {threading.current_thread().name}")
    print(f"waiting 1 seconds. thread name: {threading.current_thread().name}")
    time.sleep(1)
    print(f"1 second passed. thread name: {threading.current_thread().name}")


# target=実行したい関数, args=関数に渡す引数, name=スレッドに命名
thread_one = threading.Thread(
    target=run,
    args=("one",)
)
thread_second = threading.Thread(
    target=run,
    args=("two",),
    name="thread_second"
)

# 起動
thread_one.start()
thread_second.start()

# thread_oneが終了するのを待つ
thread_one.join()
# thread_secondが終了するのを待つ
thread_second.join()

print(threading.currentThread().name)

"""Output
>> arg: one, thread name: Thread-1
>> waiting 1 seconds. thread name: Thread-1
>> arg: two, thread name: thread_second
>> waiting 1 seconds. thread name: thread_second
>> 1 second passed. thread name: thread_second
>> 1 second passed. thread name: Thread-1
>> MainThread
"""
