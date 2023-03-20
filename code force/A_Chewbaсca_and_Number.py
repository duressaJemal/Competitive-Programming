num = list(input())

for index in range(len(num)):
    if num[index] >= "5":
        value = 9 - int(num[index])

        if not value and not index:
            continue

        if value < 0:
            continue
        
        num[index] = str(value)

print("".join(num))