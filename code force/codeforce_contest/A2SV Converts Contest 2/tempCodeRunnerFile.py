

n, m = map(int, input().split())
rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))


for letter in letters:
    
    doorms = 1
    remainder = letter

    i = 0
    while remainder > rooms[i]:
        remainder -= rooms[i]
        doorms += 1
        i += 1

    print(doorms, remainder)
