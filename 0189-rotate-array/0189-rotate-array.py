# Time: O(N)
# Space: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = k % n
        
        def reverse_list(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        nums.reverse()
        reverse_list(0, k - 1)
        reverse_list(k, n - 1)
        
        

            
        
            
            