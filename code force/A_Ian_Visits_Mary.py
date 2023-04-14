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
    a, b = inpnums()
    c_a, c_b = a, b
    n = max(a, b)
    is_prime = [True] * (n + 2)
    is_prime[0] = False
    is_prime[1] = False

    # def SieveOfEratosthenes(n):
    #     p = 2
    #     while(p * p <= n):
    #         if (is_prime[p] == True):
    #             for i in range(p * p, n + 1, p):
    #                 is_prime[i] = False
    #         p += 1
    
    # SieveOfEratosthenes(n)
    is_prime[1] = True
    # print(prime)

    if a <= 1 and b <= 1:
        print(1)
        print(a, b)
    else:
        # while a > 0 and not is_prime[a]:
        #     a -= 1
        # while b > 0 and not is_prime[b]:
        #     b -= 1
        
        print(2)
        print(a, b)
        print(c_a, c_b)
            
t = inpnum()
while t:
    main()
    t -= 1

