from collections import Counter, defaultdict


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # sort
    arr.sort()

    dic = defaultdict(int)

    for val in arr:
        dic[val] += 1
    
    
    max_count = 0
    new_arr=[]

    for val in dic:
        new_arr.append(val)
    
    count = dic[new_arr[0]]
    for i in range(1,len(new_arr)):
        if new_arr[i] - new_arr[i - 1] == 1:
            count= max(count,dic[new_arr[i]])
        else:
            max_count+=count
            count = dic[new_arr[i]]

    max_count += count
    print(max_count)
    
    return


    


t = int(input())
while t:
    solve()
    t -= 1
