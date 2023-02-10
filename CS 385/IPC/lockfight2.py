#lockfight2.py
#by Ryan Neubauer

from os import *
from random import *
from time import *
import sys

pid = getpid()

def main():
    for i in range(5):
        try:
            fd = open("/home/cs385/Desktop/IPC/neubauer.lock", 192)
            print("Process", pid, "has locked the lock")
            sleeptime = randrange(1, 10)
            print("Process", pid, "holding lock for", sleeptime, "seconds")
            sleep(sleeptime)
            print("Process", pid, "is releasing the lock")
            unlink("neubauer.lock")
            sleep(randrange(0,10))
        except:
            print("Process", pid, "found lock locked")
            sleep(3)
    sys.exit(1)
main()
