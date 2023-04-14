from bisect import bisect_left, bisect_right
from functools import lru_cache
import math
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

    a, b = inpnums()
    n = inpnum()
    
    def divisor(n):
        cur = set()
        mx = math.ceil(math.sqrt(n))   
        for index in range(1, mx + 1):
            if n % index == 0:
                cur.add(index)
                cur.add(n // index)
        return cur

    def binary_search(arr, low, high):

        left = 0
        right = len(arr) # assume valie

        while right > left + 1:

            mid = left + (right - left)
            
            if arr[mid] <= high:
                left = mid
            else:
                right = mid
            
        if low <= arr[left] <= high:
            return arr[left]
        
        return None


    a_set = divisor(a)
    b_set = divisor(b)
    common = list(divisor(a).intersection(divisor(b)))

    query = []
    for _ in range(n):
        q1, q2 = inpnums()

        best = binary_search(list(common), q1, q2)
        if best:
            print(best)
        else:
            print(-1)

main()
