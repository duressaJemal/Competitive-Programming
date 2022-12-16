# Link: https://leetcode.com/problems/valid-palindrome/
#Q: 125. Valid Palindrome

# Time: O(N)
# Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        left, right = 0, n - 1
        
        while left <= right:
            if not s[left].isalnum() or not s[right].isalnum():
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
        return True
                
            
                
