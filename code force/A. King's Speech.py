# Link: https://codeforces.com/gym/419351/problem/A
#Q: A. King's Speech

# Time: O(N)
# Space: O(N)

n = int(input())
for _ in range(n):
    output = []
    word = input()

    output.append(str(word[0]) + str(word[1]) + "... ")
    for char in word:
        output.append(char)
    
    output.append("?")
    print("".join(output))


