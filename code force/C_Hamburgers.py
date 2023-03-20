from collections import Counter, defaultdict
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

    counter = Counter(input())
    nb, ns, nc = inpnums()
    pb, ps, pc = inpnums()

    B, S, C = counter["B"], counter["S"], counter["C"]
    money = inpnum()

    value = B * pb + S * ps + C * pc
    p_b = nb * pb if B else 0
    p_s = ns * ps if S else 0
    p_c = nc * pc if C else 0

    money += (p_b + p_s + p_c) 

    print(money // value)

main()