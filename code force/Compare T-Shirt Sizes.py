# Link: https://codeforces.com/problemset/problem/1741/A
#Q: Compare T-Shirt Sizes

t = int(input())

for _ in range(t):
    left, right = list(input().split())

    if left[-1] == right[-1]:

        value = left[-1]
        if len(left) == len(right):
            print("=")
        elif len(left) > len(right):
            print(">" if value == "L" else "<")
        else:
            print("<" if value == "L" else ">")

    else:

        if left[-1] == "L":
            print(">")
        elif left[-1] == "S":
            print("<")
        else:
            if right[-1] == "L":
                print("<")
            else:
                print(">")

