s1 = list(input().split())
s2 = list(input().split())

for index, value in enumerate(s1):
    s1[index] = value.lower()

for index, value in enumerate(s2):
    s2[index] = value.lower()

if s1 < s2:
    print("-1")
elif s1 > s2:
    print("1")
else:
    print("0")