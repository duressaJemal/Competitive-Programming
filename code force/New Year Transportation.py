n, t = map(int, input().split())
a = list(map(int, input().split()))

cells , flag = 1, False
i = 0

while cells < n:
    cells += a[cells - 1]
    if cells == t:
        flag = True
        break
    i += 1

if flag:
    print("YES")
else:
    print("NO")
