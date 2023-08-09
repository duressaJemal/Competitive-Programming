class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        
        nums.sort()
        
        l, r = 0, max(nums) - min(nums)
        while l < r:
            m = (l + r) // 2
            
            pairs = 0
            prev = False
            for i in range(1, n):
                if nums[i] - nums[i - 1] <= m and not prev:
                    pairs += 1
                    prev = True
                else:
                    prev = False
            
            if pairs < p:
                l = m + 1
            else:
                r = m
        return l