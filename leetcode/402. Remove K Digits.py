# link https://leetcode.com/problems/remove-k-digits/

# time: O(n)
# space: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list(num)
        stack = []
        for n in nums:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:len(stack) - k]
        return "".join(stack).lstrip("0") or "0"
            
                
            
