

n, m = map(int, input().split())
rooms = list(map(int, input().split()))
letters = list(map(int, input().split()))
output = []

for j in range(len(letters)):
    
    if output:
        doorms = output[-1][0]
        i = doorms - 1
        remainder = output[-1][1] + (letters[j] - letters[j - 1])
    else:
        doorms = 1
        remainder = letters[j]
        i = 0
    
    while remainder > rooms[i]:
        remainder -= rooms[i]
        doorms += 1
        i += 1

    output.append((doorms, remainder))

for i in range(len(output)):
    print(output[i][0], output[i][1])

