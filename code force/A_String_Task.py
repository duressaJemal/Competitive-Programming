string = input()
output = []

vowels ={"a", "u", "e", "i", "o", "y"}

for char in string:
    char = char.lower()
    if char not in vowels:
            output.append(".")
            output.append(char)

print("".join(output))