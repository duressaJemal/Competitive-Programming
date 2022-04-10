class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
    
        container = []
        for i in range(len(nums)):
            container.append(int(nums[i]))

        container.sort()
        return str(container[-k])
        
