# Link: https://leetcode.com/problems/sliding-window-median/

# Time: O(N * K)
# Space: O(N)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        n = len(nums)
        output, small, large = [], [], []
        end = 0
        
        def remove(heap, value):
            heap[i], heap[-1] = heap[-1], heap[i]
            heap.pop()
            heapify(heap)
            
        def reorder(small, large):
            if len(small) > len(large) + 1:
                    heappush(large, -heappop(small))
            if len(small) < len(large):
                heappush(small, -heappop(large))
            
        for start in range(n - k + 1):
            
            while (len(small) + len(large)) < k:
                if not small or -small[0] >= nums[end]:
                    heappush(small, -nums[end])
                else:
                    heappush(large, nums[end])
                    
                reorder(small, large)
                end += 1
                
            if len(small) == len(large):
                output.append((-small[0] + large[0])/2)
            else:
                output.append(-small[0])
            
            value_to_remove = nums[start]
            flag = False
            
            for i in range(len(small)):
                if small[i] == -value_to_remove:
                    remove(small, i)
                    flag = True
                    break
            
            if not flag:
                for i in range(len(large)):
                    if large[i] == value_to_remove:
                        remove(large, i)
                        break
                        
            reorder(small, large)
            
        return output
            
