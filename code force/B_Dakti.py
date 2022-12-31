# Link: https://codeforces.com/gym/419351/problem/B
#Q: B_Dakti

# Time: O(N)
# Space: O(N)

t = int(input())

for _ in range(t):
    words = list(input().split())
    output = []

    for word in words:
        phrase = []
        number = 0

        for char in word:
            if char.isnumeric():
                number = char
            else:
                phrase.append(char)
        
        phrase = "".join(phrase)
        output.append((number, phrase))

    output.sort()
    res = [word[1] for word in output]
    print(*res)

    


    

