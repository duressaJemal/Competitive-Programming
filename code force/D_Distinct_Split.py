t = int(input())

while t:

    n = int(input())
    arr = input()

    u1 = set()
    u2 = set()

    for value in arr:
        if value in u1:
            u2.add(value)
        else:
            u1.add(value)
            

    print(len(u1) + len(u2))

    t -= 1


