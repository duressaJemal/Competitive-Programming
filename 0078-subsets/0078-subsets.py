class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def helper(arr, i):
            
            if i == len(nums):
                output.append(arr.copy())
                return
            
            else:
                arr.append(nums[i]) # include
                helper(arr, i + 1)
                arr.pop() # exclude
                helper(arr, i + 1)
            
            return

        helper([], 0)
        return output
                    