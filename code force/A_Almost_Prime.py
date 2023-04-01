import math

n = int(input())
total = 0

for cur in range(2, n + 1):

    right = math.ceil(math.sqrt(cur))
    count = 0

    for num in range(2, right):

        visited = False

        while cur % num == 0:
            
            cur //= num
            if not visited:
                count += 1
                visited = True
        
    if cur > 1:
        count += 1
    
    if count == 2:
        total += 1

print(total)
        

