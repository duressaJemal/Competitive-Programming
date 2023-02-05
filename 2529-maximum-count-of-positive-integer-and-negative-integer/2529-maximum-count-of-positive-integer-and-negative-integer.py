class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        pos_count = 0
        neg_count = 0
        
        for value in nums:
            if value < 0:
                neg_count += 1
            elif value > 0:
                pos_count += 1
        
        return max(pos_count, neg_count)