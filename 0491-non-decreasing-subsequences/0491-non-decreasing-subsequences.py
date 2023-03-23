class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        
        def backtrack(arr, indx):
            
            if indx == len(nums):
                if len(arr) >= 2:
                    output.add(tuple(arr))
                return
            
            value = nums[indx]
            
            if not arr or arr[-1] <= value:
                arr.append(value)
                backtrack(arr, indx + 1)
                arr.pop()
            backtrack(arr, indx + 1)
            
            return
        
        backtrack([], 0)
        res = []
        
        for val in output:
            res.append(list(val))
        
        return res
        
        
        
                    