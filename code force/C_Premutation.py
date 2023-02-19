t = int(input())

while t:

    n = int(input())
    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    # if n == 3:
    #     answer = []
    #     if arr[1][0] == arr[2][0]:
    #         answer = arr[1][:1]+arr[0]
    #     elif arr[1][0] == arr[0][0]:
    #         answer = arr[1][:1] + arr[2]
    #     else:
    #         answer = arr[2][:1] + arr[1]
    # else:
    
    #     # do check from forward
    #     for i in range(n-1):
    #         for j in range(i + 1, n):
    #             valid = True
    #             for _ in range(n-2):
    #                 if arr[i][_] != arr[j][_]:
    #                     valid = False
    #                     break
    #             if valid:
    #                 answer = arr[i][::]
    #                 answer.pop()
    #                 break
    #         if valid:
    #             break

    #     for i in range(n-1):
    #         for j in range(i + 1, n):
    #             valid = True
    #             for _ in range(n-2,n-4,-1):
    #                 if arr[i][_] != arr[j][_]:
    #                     valid = False
    #                     break

    #             if valid:
    #                 answer.extend(arr[i][-2:])
    #                 break
    #         if valid:
    #             break
    # print(*answer)

    max_total = n * (n + 1) // 2
    first_missing = max_total - sum(arr[0])
    insertion_index = 0

    dic = {}
    for index in range(n - 1):
        dic[arr[0][index]] = index + 1

    for index in range(n - 1):
        if arr[1][index] == first_missing:
            insertion_index = index
            break
        else:
            dic[arr[1][index]] -= 1

    second_mising = max_total - sum(arr[1])
    #####

    for index in range(n - 1):
        if index <= insertion_index:
            if arr[2][index] == second_mising:
                    dic[arr[2][index]] -= 1
            break
    
    output = [0] * n
    for key, value in dic.items():
        output[value] = key
    
    output[insertion_index] = first_missing
    print(*output)
    t-= 1
