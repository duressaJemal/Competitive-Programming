# link https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        smallest, largest = collections.deque([]), collections.deque([])
        window, right , left = 0, 0, 0
        
        while right < len(nums):
            
            # inceasing monotonic queue
            while smallest and nums[right] < smallest[-1]:
                smallest.pop()
            smallest.append(nums[right])
            
            # decreasing monotonic queue
            while largest and nums[right] > largest[-1]:
                largest.pop()
            largest.append(nums[right])
            
            # for moving the left pointer
            while largest[0] - smallest[0] > limit:
                if nums[left] == smallest[0]:
                    smallest.popleft()
                
                if nums[left] == largest[0]:
                    largest.popleft()
                
                left += 1
                
            else:
                window = max(window, (right - left + 1))
                right += 1
            
        return window
