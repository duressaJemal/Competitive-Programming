# Link: https://leetcode.com/problems/longest-palindrome/
#Q: 409. Longest Palindrome

# Time: O(N)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        counter = Counter(s)
        odd_length = 0
        
        total = 0
        added_odd = False
        
        for key in counter:
            if counter[key] % 2 == 0:
                total += counter[key]
            else:
                if added_odd:
                    total += counter[key] - 1
                else:
                    total += counter[key]
                    added_odd = True
            
        return total
