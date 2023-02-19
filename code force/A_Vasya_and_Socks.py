n, m = map(int, input().split())

days = n
current_day = 0

while current_day < days:
    
    current_day += 1
    if current_day % m == 0:
        days += 1

print(current_day)

