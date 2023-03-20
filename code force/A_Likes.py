from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

def inp():
    return stdin.readline()

def inpnum():
    return int(stdin.readline())

def inpli():
    return list(map(int, stdin.readline().strip().split()))

def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])

def inpnums():
    return map(int, stdin.readline().strip().split())

def main():

    n = inpnum()
    arr = inpli()

    pos_count = 0
    neg_count = 0

    # count
    for val in arr:
        if val > 0:
            pos_count += 1
        else:
            neg_count += 1
    
    p_count = pos_count
    n_count = neg_count

    mx = []
    curr = 1
    pos_count -= 1
    mx.append(1)

    for _ in range(n - 1):

        if pos_count:
            curr += 1
            mx.append(curr)
            pos_count -= 1
        else:
            if neg_count:
                curr -= 1
                mx.append(curr)
                neg_count -= 1
    
    pos_count = p_count
    neg_count = n_count
    mn = []
    curr = 0
    for _ in range(n):
        if curr:
            if neg_count:
                neg_count -= 1
                curr -= 1
            else:
                curr += 1
        else:
            curr += 1
        mn.append(curr)

 


    print(*mx)
    print(*mn)


            

        

    
        
t = inpnum()
while t:
    main()
    t -= 1

