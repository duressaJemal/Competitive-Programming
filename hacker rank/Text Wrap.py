# Link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=false
#Q: Text Wrap

# Time: O(N)
# Space: O(N)

def wrap(string, max_width):
    output = []
    count = 0
    
    n = len(string)
    for i in range(n):
        if count == max_width:
            output.append("\n")
            count = 0
        output.append(string[i])
        count += 1

    return "".join(output)

if __name__ == '__main__':
