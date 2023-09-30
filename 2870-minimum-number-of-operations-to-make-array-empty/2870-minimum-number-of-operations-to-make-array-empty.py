class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        mn = 0
        
        for key in counter:
            value = counter[key]
            if value == 1:
                return -1
            else:

                mn += (value // 3)
                if value % 3 != 0:
                    mn += 1
        
        return mn