# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Time: O(log(N))
# Space: (N)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        
        def binarySearch(nums, target, low, high, find_first):
            
            position = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    position = mid
                    if find_first:   
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return position
    
        return [binarySearch(nums, target, 0, n - 1, True), binarySearch(nums, target, 0, n - 1, False)] if nums else [-1, -1]
        
