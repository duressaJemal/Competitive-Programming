# Link: https://leetcode.com/problems/count-good-meals/
#Q: 1711. Count Good Meals

# Time: O(N*26)
# Space: O(N)

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        counter = Counter(nums)
        output = 0
        
        for i in range(len(nums)):
            for j in range(22):
                y = 2 ** j - nums[i]
                if y in counter:
                    if y == nums[i]:
                        output += counter[y] - 1
                    else:
                        output += counter[y]
                        
        return (output // 2) % (10 ** 9 + 7)
        
             
# Alternative

# Time: O(N*26)
# Space: O(N)

class Solution:
    def countPairs(self, nums: List[int]) -> int:
      
        counter = Counter(nums)
        output = 0
        
        for i in range(len(nums)):
            for j in range(22):
                y = 2 ** j - nums[i]
                if y in counter:
                    if y == nums[i]:
                        output += counter[y] - 1
                    else:
                        output += counter[y]
            counter[nums[i]] -= 1
        
        return output % (10 ** 9 + 7)
    
            
            
            
          
