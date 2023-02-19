t = int(input())
arr = []
for i in range(t):
    arr.append(input())

for string in arr:

    # Slidding window
    n = len(string)
    dic = {}
    end, shortest = 0, float("inf")
    flag = False
    
    for start in range(n):

        while len(dic) < 3:
            if end == n:
                if start == 0:
                    flag = True
                break

            if string[end] in dic:
                dic[string[end]] += 1
            else:
                dic[string[end]] = 1
            end += 1
        
        if flag:
            break

        shortest = min(shortest, end - start)
        dic[string[start]] -= 1
        if not[dic[string[start]]]:
            dic.pop(string[start])

    if shortest == float("inf"):
        print(0)
    else:
        print(shortest)





            
            






