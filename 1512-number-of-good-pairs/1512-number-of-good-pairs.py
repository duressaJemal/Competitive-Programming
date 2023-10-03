class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        counter = Counter(nums)
        
        for num in nums:
            count += (counter[num] - 1)
            counter[num] -= 1
        
        return count