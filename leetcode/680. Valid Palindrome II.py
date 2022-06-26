# link: https://leetcode.com/problems/valid-palindrome-ii/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome_check(s, start, end):
        
            while start < end:
                if s[start] != s[end]:
                    return False
            
                start += 1
                end -= 1
                
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            
            if s[left] != s[right]:
                return palindrome_check(s, left, right - 1) or palindrome_check(s, left + 1, right)
            left += 1
            right -= 1
            
        return True
