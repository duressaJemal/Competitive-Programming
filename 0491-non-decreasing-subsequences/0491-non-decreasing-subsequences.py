class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def backtrack(arr, indx):
            
            # base case
            if indx == len(nums):
                if len(arr) >= 2 and arr not in output:
                    output.append(arr.copy())
                return
            
            value = nums[indx]
            
            if not arr or arr[-1] <= value:
                arr.append(value)
                backtrack(arr, indx + 1)
                arr.pop()
            backtrack(arr, indx + 1)
            
            return
        
        backtrack([], 0)
        return output
        
        
        
                    