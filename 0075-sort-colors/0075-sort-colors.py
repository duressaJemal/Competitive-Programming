# Follow-up (Counting sort)

# Time: O(N)
# Space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        n = len(nums)
        
        counter = Counter(nums)
        
        zeros_count = counter[0]
        ones_count = counter[1]
        
        for index in range(n):
            if zeros_count:
                nums[index] = 0
                zeros_count -= 1
            elif ones_count:
                nums[index] = 1
                ones_count -= 1
            else:
                nums[index] = 2
        

        
# Time: O(N^2) (Insertion sort)
# Space: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                for i in range(index, 0, -1):
                    if nums[i] < nums[i - 1]:
                        nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    else:
                        break
        
                        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        