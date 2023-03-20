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

    input()
    n, k = inpnums()
    position = inpli()
    temp = inpli()

    def assign_values(index, curr_temp, temp_pos):

        if index in dic:
            if not curr_temp:
                curr_temp = dic[index] 
                temp_pos = index
            else:
                value = curr_temp + abs(temp_pos - index)
                if value >= dic[index]:
                    curr_temp = dic[index]
                    temp_pos = index
        
        return curr_temp, temp_pos

    dic = {}

    for index in range(k):
        dic[position[index]] = temp[index]
    
    arr = [float("inf")] * n

    curr_temp = 0
    temp_pos = 0

    for index in range(1, n + 1):
        curr_temp, temp_pos = assign_values(index, curr_temp, temp_pos)
        if curr_temp:
            arr[index - 1] = min(arr[index - 1], curr_temp + abs(index - temp_pos))
        else:
            continue
    
    curr_temp = 0
    temp_pos = 0

    for index in range(n, 0, - 1):
        curr_temp, temp_pos = assign_values(index, curr_temp, temp_pos)
        if curr_temp:
            arr[index - 1] = min(arr[index - 1], curr_temp + abs(index - temp_pos))
        else:
            continue

    print(*arr)

t = inpnum()
while t:
    main()
    t -= 1

