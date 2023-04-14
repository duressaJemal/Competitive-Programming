from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

def inp(): return stdin.readline()
def inpnum(): return int(stdin.readline())
def inpli(): return list(map(int, stdin.readline().strip().split()))
def inpst():
    s = stdin.readline().strip()
    return list(s[:len(s)])
def inpnums():return map(int, stdin.readline().strip().split())
def main():
    
    n = inpnum()
    
    row1 = [0] * n
    row2 = [0] * n

    cur_index = 0
    for value in range(2 * n, n, -2):
        if cur_index < n:
            row1[cur_index] = value
            cur_index += 2

    cur_index = 1
    for value in range(2, n + 1, 2):
        if cur_index < n:
            row1[cur_index] = value
            cur_index += 2
    

    cur_index = 0
    for value in range(1, 2 ** n + 1, 2):
        if cur_index < n:
            row2[cur_index] = value
            cur_index += 2
    
    cur_index = 1
    for value in range(n + 1, 2 ** n + 1, 2):
        if cur_index < n:
            row2[cur_index] = value
            cur_index += 2

    print(*row1)
    print(*row2)



t = inpnum()
while t:
    main()
    t -= 1

