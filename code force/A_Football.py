string = input()
n = len(string)

max_length = 0

left = 0
for right in range(n):
    while string[right] != string[left]:
        left += 1
    max_length = max(max_length, right - left + 1)

if max_length >= 7:
    print("YES")
else:
    print("NO")
