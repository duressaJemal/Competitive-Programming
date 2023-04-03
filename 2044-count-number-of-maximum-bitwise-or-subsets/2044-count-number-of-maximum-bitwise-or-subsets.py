# Time: O(2^N)
# Space: O(N^2)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        
        def backtrack(index, arr):
            """
            Generate all subsets
            """
            if index == n:
                if arr:
                    subsets.append(arr.copy())
                return
            
            # include
            arr.append(nums[index])
            backtrack(index + 1, arr)
            
            # exclude
            arr.pop()
            backtrack(index + 1, arr)
            
            return
        
        # find OR
        def find_or(arr):
            """
            find Bitwise OR of array
            """
            cur = 0
            for val in arr:
                cur |= val
            
            return cur
        
        
        # generate all subsets
        subsets = []
        backtrack(0, [])
        
        # find max OR
        mx = find_or(nums)
        
        for arr in subsets:
            if find_or(arr) == mx:
                count += 1
        
        return count
        
        
        
        
        
        
        
            
        
            
        
        