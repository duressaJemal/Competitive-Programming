class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        bar = len(nums) // 3
        output = []
        
        for key in counter:
            if counter[key] > bar:
                output.append(key)
        
        return output