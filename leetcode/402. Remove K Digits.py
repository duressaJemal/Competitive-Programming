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
        if len(stack) == 0:
            return "0"
        return str(int("".join(stack)))
