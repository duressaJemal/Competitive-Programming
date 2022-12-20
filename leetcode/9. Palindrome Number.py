# Link: https://leetcode.com/problems/palindrome-number/
#Q: 9. Palindrome Number

# Time: O(log10(N))
# Space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        if 0 <= x <= 9: return True
        
        original = x
        
        generated = 0
        while x > 0:
            generated = generated * 10 + (x % 10)
            x //= 10
        return generated == original
        
        
        
