# Link: https://codeforces.com/problemset/problem/1251/A
#Q: Rebellion

# Time: O(N) -- size(string)
# Space: O(1)

def solve():
    a = input()
    n = len(a)
    res = [0] * 26

    i = 0
    while i < n:
        j = i 
        expanded = False
        while j + 1 < n and a[j + 1] == a[j]:
            j += 1
            expanded = True

        length = j - i + 1
        if (length % 2 != 0): # if lenght not even
            res[ord(a[i]) - ord("a")] = 1

        if expanded:
            i = j + 1
        else:
            i += 1
    
    for i in range(26):
        if res[i] == 1:
            print(chr(i + ord("a")) , end = "")
    print()


t = int(input())
while t:
    solve()
    t -= 1
    
