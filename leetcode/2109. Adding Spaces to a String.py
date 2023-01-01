# Link: https://leetcode.com/problems/adding-spaces-to-a-string/
#Q: 2109. Adding Spaces to a String

# Time: O(N + M) where N = len(s) and M = len(spaces)
# Space: O(N + M)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        spaces = set(spaces)
        
        output = []
        
        for index in range(n):
            if index in spaces:
                output.append(" ")
            output.append(s[index])
        
        return "".join(output)

# Time: O(N + Mlog(M))
# Space: O(N + M)

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        spaces.sort()
        
        output = []
        
        spaces_index = 0
        for index in range(n):
            if spaces_index < len(spaces) and index == spaces[spaces_index]:
                output.append(" ")
                spaces_index += 1
            output.append(s[index])
        
        return "".join(output)
