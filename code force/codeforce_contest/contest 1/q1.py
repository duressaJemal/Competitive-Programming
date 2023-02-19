n, k = map(int, input().split())

total_minutes = 4 * 60
time_left = total_minutes - k

i = 1
count = 0
SUM = 0

while i <= n:
    SUM += (5 * i)
    if SUM <= time_left:
        count += 1
        i += 1
    else:
        break

print(count)










