#TwoPipeSum.py
#by Ryan Neubauer

import os
import random

def main():
    r, w = os.pipe()
    childa = os.fork()
    if childa == 0:
        os.close(r)
        w = os.fdopen(w, "w")
        buffer = str(random.randint(0, 100))
        print(buffer, flush=True, file=w)
    else:
        os.close(w)
        r2, w2 = os.pipe()
        childb = os.fork()
        if childb == 0:
            os.close(r)
            os.close(r2)
            w2 = os.fdopen(w2, "w")
            buffer = str(random.randint(0, 100))
            print(buffer, flush=True, file=w2)
        else:
            os.close(w2)
            os.wait()
            os.wait()
            r = os.fdopen(r)
            r2 = os.fdopen(r2)
            n1 = int(r.readline()[:-1])
            n2 = int(r2.readline()[:-1])
            print(f"[{os.getpid()}]: spawning children")
            print(f"[{childa}]: picks {n1}")
            print(f"[{childb}]: picks {n2}")
            print("Sum is:", n1 + n2)

main()
        
