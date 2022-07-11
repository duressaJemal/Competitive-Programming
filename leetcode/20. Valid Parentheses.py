# link: https://leetcode.com/problems/valid-parentheses/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        tags = {")":"(", "]":"[", "}":"{"}
        stack = [0]
        
        for i in s:
            if i in tags:
                if stack.pop() != tags[i]:
                    return False
            else:
                stack.append(i)
            
        return len(stack) == 1
            

        
