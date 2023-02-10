#lockfight.py
#by Ryan Neubauer

from _thread import *
from random import *
from time import sleep

lock = allocate_lock()
isdone = False

def getlock(threadname):
    global lock
    global isdone
    for i in range(5):
        lock.acquire()
        sleeptime = randrange(1, 6)
        print(threadname, "Has the lock")
        print(threadname, "holding the lock for", sleeptime, "seconds")
        sleep(sleeptime)
        print(threadname, "Has released the lock")
        lock.release()
        sleep(1)
    isdone = True

def main():
    thread0 = start_new_thread(getlock, ("Thread 0",))
    thread1 = start_new_thread(getlock, ("Thread 1",))
    while isdone != True and lock.locked != False:
        pass
    print("Main thread exiting...")
    exit()
    
main()

