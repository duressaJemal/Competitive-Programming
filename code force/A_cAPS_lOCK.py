string = input()
n = len(string)

is_valid = True
for index in range(n):
    if string[index].islower() and index != 0:
        is_valid = False
        break

if is_valid:
    output = []
    for char in string:
        if char.islower():
            output.append(char.upper())
        else:
            output.append(char.lower())
    print("".join(output))
else:
    print(string)
