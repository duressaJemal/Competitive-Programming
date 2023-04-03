# Time: O(2^N)
# Space: O(N^2)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        def backtrack(index, cur):
            """
            Generate all subsets
            """
            if index == n:
                subsets.append(cur)
                return
            
            # include
            include = cur | nums[index]
            backtrack(index + 1, include)
            
            # exclude
            backtrack(index + 1, cur)
            
            return
        
        
        # generate all subsets
        subsets = []
        backtrack(0, 0)
        
        subsets.sort(reverse = True)
        mx = subsets[0]
        
        for val in subsets:
            if val == mx:
                count += 1
            else:
                break

        return count
        
        
        
        
        
        
        
            
        
            
        
        