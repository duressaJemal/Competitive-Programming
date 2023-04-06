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
    not_source = set()
    source = []
    sink = []

    for i in range(n):
        row = inpli()
        is_sink = True

        for index in range(n):
            if row[index] == 1:
                is_sink = False
                not_source.add(index + 1)
        
        if is_sink:
            sink.append(i + 1)
    
    for node in range(1, n + 1):
        if node not in not_source:
            source.append(node)

    sink.sort()
    source.sort()

    print(len(source), *source)
    print(len(sink), *sink)
            
main()

