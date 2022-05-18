# link https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        num = list(num)
        stack = []
        
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # slices the list if k > 0
        stack = stack[:len(stack)-k]
        
        return "".join(stack).lstrip("0") or "0"
