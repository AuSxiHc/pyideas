#Your mind shall be blown...
import time as t
import os

loadinglen = 5

input()

for i in range(0,loadinglen):
    print("[",sep="",end="")
    for j in range(0,i):
        print("=",sep="",end="")
        t.sleep(0.5)
        os.system('cls')
    print("]",sep="",end="")