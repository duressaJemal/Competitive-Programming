class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        end = len(s) - 1
        counter = 0
        
        while s[end] == " ":
            end -= 1
        
        while end >= 0 and s[end] != " ":
            counter += 1
            end -= 1
        
        return counter
        
        
