class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        def merge(left, right):
            
            i = 0
            j = 0
            
            c = [0] * (len(right) + len(left))
            total = 0
            
            while i < len(left) or j < len(right):
                
                # value at left is less than or equal to value at right
                if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                    
                    index = left[i][1]
                    cur = total - i
                    count[index] += cur
                    c[i + j] = left[i]
                    i += 1
                else:
                    # value at right less than value at left
                    c[i + j] = right[j]
                    j += 1
                
                total += 1
                     
            return c
        
        def merge_sort(l, r):
            
            # base case
            if l == r:
                return [nums[l]]
            
            mid = l + (r - l) // 2
            
            left_val = merge_sort(l, mid)
            right_val = merge_sort(mid + 1, r)
            
            combined = merge(left_val, right_val)
            
            return combined
        
        n = len(nums)
        
        for index, value in enumerate(nums):
            nums[index] = (value, index)
        count = [0] * n
        merge_sort(0, n - 1)
        return count
        
            
            