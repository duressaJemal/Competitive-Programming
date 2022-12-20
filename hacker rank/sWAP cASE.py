# Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=false
#Q: sWAP cASE

# Time: O(N)
# Space: O(N)

def swap_case(s):
    output = []
    for i in range(len(s)):
        if ord("A") <= ord(s[i]) <= ord("Z"):
            output.append(s[i].lower())
        elif ord("a") <= ord(s[i]) <= ord("z"):
            output.append(s[i].upper())
        else:
            output.append(s[i])
            
    return "".join(output)
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
