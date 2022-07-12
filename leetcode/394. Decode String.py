# link: https://leetcode.com/problems/decode-string/submissions/

# RECURSION

# time: O(n)
# space: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        
        n = len(s)
        
        def helper(s, index):
            num = 0
            result = []
            while index < n:
                if s[index].isdigit():
                    num = num * 10 + int(s[index])
                elif s[index] == "[":
                    ans, i =   helper(s, index + 1)
                    result += num * ans
                    index, num = i, 0
                elif s[index] == "]":
                    return result, index 
                else:
                    result.append(s[index])  
                index += 1
            return result
        return "".join(helper(s, 0))
            
# STACK

# time: 
# space: 

class Solution:
    def decodeString(self, s: str) -> str:
        
        n = len(s)
        end = 0
        stack = []
        
        while end < n:
            
            if s[end] == "]":
                values = []
                digit = ""
                while not stack[-1].isdigit():
                    values.append(stack.pop())
                    
                while stack and stack[-1].isdigit():
                    digit += stack.pop()
                    
                values.pop() # for removing the openning tag
                stack += int(digit[::-1]) * values[::-1] 
            else:
                stack.append(s[end])
            end += 1
        
        return "".join(stack)
        
        
        
            
