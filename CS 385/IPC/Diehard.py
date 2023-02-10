#Diehard.py
#By Ryan Neubauer

from signal import *
import sys, os, time

def handler(sig, tb):
    print("Caught Signal:", sig)

def main():
    print("My PID is:", os.getpid())
    print("Hit me! You can't kill me!")
    hits = 0
    for i in range(1, NSIG):
        if i not in [9, 19, 32, 33]:
            signal(i, handler)
    while hits < 5:
        pause()
        hits += 1
        print("Hits:", hits)
    print("AH! I guess you can kill me...")
main()
