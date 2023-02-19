string = input()
key_characters = {"H", "Q", "9"}

is_valid = False

for char in string:
    if char in key_characters:
        is_valid = True
        break

if is_valid:
    print("YES")
else:
    print("NO")