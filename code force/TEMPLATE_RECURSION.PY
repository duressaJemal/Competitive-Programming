from functools import lru_cache
import threading
from sys import stdin,stdout,setrecursionlimit

# setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)

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
    ...

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()


