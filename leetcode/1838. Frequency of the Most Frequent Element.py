class Solution:
    def maxFrequency(self, nums, k):

            if len(nums) == 1:
                return 1
            
            nums.sort()
            addition, start ,end, largest = nums[0] + nums[1], 0, 1, 1
           
            while(end < len(nums)):
                
                if(addition + k) >= (end - start + 1) * nums[end]:
                    
                    largest = max(largest, (end - start + 1))
                    end += 1
                    
                    if end < len(nums):
                        addition += nums[end]
                
                else:
                    
                    if start == end:
                        end += 1
                        continue
                    
                    addition -= nums[start]
                    start += 1
            
            return largest
