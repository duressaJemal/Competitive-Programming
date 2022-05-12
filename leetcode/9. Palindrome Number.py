#link https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        generated = 0
        while x > generated:
            generated = generated * 10 + x % 10
            x = x // 10
        
        return x == generated or x == generated // 10
