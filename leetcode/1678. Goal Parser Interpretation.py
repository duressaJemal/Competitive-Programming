# Link: https://leetcode.com/problems/goal-parser-interpretation/
#Q: 1678. Goal Parser Interpretation

# Time: O(N)
# Space: O(N)

class Solution:
    def interpret(self, command: str) -> str:
        
        output, i = [], 0
        while i < len(command):
            if command[i] == "G":
                output.append("G")
                i += 1
            else:
                if command[i + 1] == ")":
                    output.append("o")
                    i += 2
                else:
                    output.append("al")
                    i += 4
                    
        return "".join(output)
