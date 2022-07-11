# link: https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/submissions/

# time: O(n ** 2)
# space: O(n)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        popped = []
        
        for i in s:
            if i == ")":
                while stack[-1] != "(":
                    popped.append(stack.pop())
                stack.pop()
                stack += popped
                popped = []
                    
            else:
                stack.append(i)
        
        return "".join(stack)
        
# CHECKOUT THE OPTIMIZED (O(n)) SOLUTION
