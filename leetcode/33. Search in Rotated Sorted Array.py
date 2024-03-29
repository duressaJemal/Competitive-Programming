# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Binary search

# Time: O(log(N))
# Space: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        start, end = 0, n - 1
        
        while start < end:
            
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return start if nums[start] == target else -1
                
                
