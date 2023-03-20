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
    n, k = inpnums()
    arr = inpli()

    def solve(k, index):
        
        # base case
        if not k: return 0

        nums_to_right = length - (index + 1)
        itr = min(k, nums_to_right)

        # for next iteration
        k -= itr
        current = itr * arr[index]
        next_index = index + (nums_to_right // 2)

        return current+ solve(k, next_index)
    
    length = 2 ** n
    arr.sort()
    total_time = solve(k, (length // 2) - 1)
    
    print(total_time)
    return

main()
# t = inp()
# while t:
#     main()
#     t -= 1


