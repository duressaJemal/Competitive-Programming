class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        
        def backtrack(arr, bit, count):
            
            if count == n:
                res.append(arr.copy())
                return
                
            for index in range(n):
                
                if bit & (1 << index) == 0:
                    
                    # set the index's bit to 1
                    bit |= (1 << index)
                    arr.append(nums[index])
                    backtrack(arr, bit, count + 1)
                    
                    # set the index's bit to 0
                    bit ^= (1 << index)
                    arr.pop()
                
            return
        
        backtrack([], 0, 0)
        return res
            


            
                    
                    
            
                
            