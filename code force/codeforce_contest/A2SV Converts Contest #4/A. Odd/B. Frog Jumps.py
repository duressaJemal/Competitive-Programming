# Link: https://codeforces.com/gym/396419/problem/B
#q : B. Frog Jumps

# t = int(input())
# def is_valid(d, string):
#     d -= 1
#     current_index = d

#     if string[current_index] == "R":
#         current_index += d
#     else:
#         for i in range(current_index, min(0, current_index - d) - 1, -1):
#             # case1 :
#             if string[i] == "R":
#                 current_index = i
#                 break

    

# for _ in range(t):
#     string = input()
#     n = len(string)
#     left = 0 # initail invalid
#     right = n + 1 # assume first valid

#     while right > left + 1:
#         mid = (left + right) // 2
#         if is_valid(mid, string):
#             right = mid
#         else:
#             left = mid
    
#     print(right)

# Time: O(N)
# Space: O(1)

t = int(input())
for _ in range(t):
    string = input()

    longest = 0
    number_l = 0

    for i in range(len(string)):

        if string[i] == "L":
            number_l += 1
            longest = max(longest, number_l)
        else:
            number_l = 0
    print(longest + 1)

            

        
    
    
