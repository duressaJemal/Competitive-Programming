class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(string, left, right):
            is_valid = True
            while left <= right:
                if string[left] != string[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True
        
        
        n = len(s)
        left = 0
        right = n - 1
        
        while left <= right:
            if s[left] != s[right]:
                return palindrome(s, left + 1, right) or palindrome(s, left, right - 1)
            else:
                left += 1
                right -= 1
        
        return True