# 1. Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.


import threading
def worker():
    print("Hello from worker thread")
t1 = threading.Thread(target=worker)
t1.start()
print("Hello from main thread")
t1.join()


# 2. Write a Python program that creates three separate threads where each
# thread prints numbers from 1 to 5, and every printed number must be prefixed
# with the name of the thread that printed it, such as “Thread-1: 3”.



import threading

def thread1(n):
    for i in range(1,n+1):
        print("Thread-1 :",i)
def thread2(n):
    for i in range(1,n+1):
        print("Thread-2 :",i)
def thread3(n):
    for i in range(1,n+1):
        print("Thread-3 :",i)
t1 = threading.Thread(target=thread1,args=(5,))
t2 = threading.Thread(target=thread2,args=(5,))
t3 = threading.Thread(target=thread3,args=(5,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()





# 3. Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.


import threading
def worker(n1,n2):
    print("args sum",n1+n2)
t1 = threading.Thread(target=worker,args=(4,6,))
t1.start()
print("Main thread is starting")
t1.join()






# 4. Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.


import threading
counter=0
def worker():
    global counter
    for i in range(10000):
        counter+=1
t1=threading.Thread(target=worker)
t2=threading.Thread(target=worker)
t1.start()
t2.start()
t1.join()
t2.join()
print("Main thread",counter)




# 5. Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct.

import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    for i in range(100000):
        with lock:
            counter += 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print("Final counter:", counter)



# 6. Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.


import threading
import time
def thread1():
    print("Thread1 started")
    time.sleep(2)
    print("Thread1 ended")
def thread2():
    print("Thread2 started")
t1=threading.Thread(target=thread1)
t2=threading.Thread(target=thread2)
t1.start()
t1.join()
t2.start()
t2.join()
print("Mian thread")
