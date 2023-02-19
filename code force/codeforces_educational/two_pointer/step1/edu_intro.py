a=[1,3,5,8,10]
b=[2,6,7,9,13]
c = [0] * (len(a) + len(b))

i = 0
j = 0

while i < len(a) or j < len(b):
    if j == len(b) or i < len(a) and a[i] < b[j]:
        c[i + j] = a[i]
        i += 1
    else:
        c[i + j] = b[j]
        j += 1
print(c)

