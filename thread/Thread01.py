#Python Thread 예제1
import threading
import time


def execute(number):
    """
    쓰레드에서 실행 할 함수
    """
    time.sleep(number)
    print(threading.currentThread().getName(), number)

def execute_noThread(number):
    """
    쓰레드에서 실행 할 함수
    """
    time.sleep(number)
    print(threading.currentThread().getName(), number)


if __name__ == '__main__':
    for i in range(1,36): # 1 ~ 7 실행
        my_thread = threading.Thread(target=execute, args=(i,))
        my_thread.start()

    for i in range(1,8): # 1 ~ 7 실행
        no_thread = execute_noThread(i)
