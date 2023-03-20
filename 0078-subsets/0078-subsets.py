class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        subset = []
        
        def helper(i):
            if i == len(nums):
                output.append(deepcopy(subset))
            else:
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()
                helper(i + 1)
                

        helper(0)
        return output
                    