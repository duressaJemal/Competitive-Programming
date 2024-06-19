class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        
        left = 0
        length = 0
        
        arr = [1, 2, 3]
        
        def check(left, right):
            counter = Counter(s[left:right + 1])
            for key in counter:
                if counter[key] > 1:
                    return False
            return True
        
        for right in range(len(s)):
        
            # add
        
            # check
            if check(left, right):
                length = max(length, right - left + 1)
                continue
            else:
                left += 1
                
            
        return length


            