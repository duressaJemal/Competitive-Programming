class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        d = {0:0}
        start = 0
        end = 0
        longest = 0
        
        while end < len(nums) and start < len(nums):
            
            if d[0] <= k:
                
                if nums[end] == 0:
                    d[0] += 1
                    
                if d[0] <= k:
                    longest = max(longest, end-start + 1)
                    end += 1
                    
            else:
                if nums[start] == 0:
                    d[0] -= 1

                if start == end:
                    start += 1
                    end += 1
                    continue
                    
                if d[0] <= k:
                    end += 1
                    start += 1
                    continue
                start += 1
                
        return longest
