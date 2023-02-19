n = int(input())
arr = []

for i in range(n):
    arr.append(input())

output = []

for num in arr:
    if int(num) % 2 == 0:
        output.append(0)
    
    elif int(num[0]) % 2 == 0:
        output.append(1)
    else:
        i = 0
        flag = False
        while i < len(num):
            if int(num[i]) % 2 == 0:
                output.append(2)
                flag = True
                break
            i += 1
        if not flag:
            output.append(-1)
        
for num in output:
    print(int(num))
                
        




