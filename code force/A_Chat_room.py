string = input()
order = ["o", "l", "l", "e", "h"]

for value in string:
    if order and value == order[-1]:
        order.pop()

if order:
    print("NO")
else:
    print("YES")