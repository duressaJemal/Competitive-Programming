def solve():
    n, m = map(int, input().split())
    arr = list(input())

    for itr in range(min(m, 1000)):
        temp = arr.copy()
        
        for index in range(n):

            if arr[index] == "0":
                if index == 0:
                    if arr[index + 1] == "1":
                        temp[index] = "1"

                elif index == n - 1:
                    if arr[index - 1] == "1":
                        temp[index] = "1"

                else:
                    adj = [arr[index - 1], arr[index + 1]]
                    if "0" in adj and "1" in adj:
                        temp[index] = "1"
            else:
                continue
        arr = temp
    print("".join(arr))
    return

t = int(input())
while t:
    solve()

    t -= 1


    # one_in_array = 1 in arr

    # one_index = -1001
    # left_distance = {}
    # # distance to left
    # for index in range(n):
    #     if not arr[index]:
    #         distance = index - one_index
    #         left_distance[index] = distance
    #     else:
    #         one_index = index
    
    # one_index = 1001
    # right_distance = {}
    # # distance to the right
    # for index in range(n - 1, -1, -1):
    #     if not arr[index]:
    #         distance = one_index - index
    #         right_distance[index] = distance
    #     else:
    #         one_index = index
    
    # output = []

    # for index in range(n):
    #     if not arr[index]:
    #         l_distance = left_distance[index]
    #         r_distance = right_distance[index]

    #         if l_distance == r_distance:
    #             output.append("0")
    #         else:
    #             min_distance = min(l_distance, r_distance)
    #             if min_distance <= m and one_in_array:
    #                 output.append("1")
    #             else:
    #                 output.append("0")
    #     else:
    #         output.append("1")

    # print("".join(output))


