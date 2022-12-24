# Link: https://codeforces.com/gym/418150/problem/C
#Q: Haile

# Time: O(N)
# Space: O(N)

n = int(input())
for _ in range(n):
    output = []
    data = input()
    for i in range(len(data)):
        if data[i] == "#":
            output.append(" ")
        else:
            output.append(data[i])
    
    print("".join(output))
    
