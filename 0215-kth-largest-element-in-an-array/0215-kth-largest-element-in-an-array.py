class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ofset = 10 ** 4
        arr = [0] * (2 * (10 ** 4) + 1)
        
        for val in nums:
            arr[ofset + val] += 1
    
        cur_sum = 0
        for index in range(len(arr) - 1, -1, -1):
            cur_sum += arr[index]
            if cur_sum >= k:
                return index - ofset
            
        
        