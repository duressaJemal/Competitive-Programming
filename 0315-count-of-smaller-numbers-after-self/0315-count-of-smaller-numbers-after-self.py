# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            """
            merge two sorted arrays of index
            sorted by the value of would fetch not directly
            
            """
            
            i = 0
            j = 0
            
            c = [0] * (len(right) + len(left))
            right_count = 0
            
            while i < len(left) or j < len(right):
                
                # value at left is less than or equal to value at right
                if j >= len(right) or (i < len(left) and nums[left[i]] <= nums[right[j]]):
                    count[left[i]] += right_count
                    c[i + j] = left[i]
                    i += 1
            
                else:
                    
                    # value at right less than value at left
                    c[i + j] = right[j]
                    right_count += 1
                    j += 1
                     
            return c
        
        def merge_sort(l, r):
            
            # base case
            if l == r:
                return [nums_index[l]]
            
            mid = l + (r - l) // 2
            
            left_val = merge_sort(l, mid)
            right_val = merge_sort(mid + 1, r)
            
            combined = merge(left_val, right_val)
            
            return combined
        
        n = len(nums)
        nums_index = [ x for x in range(n)]
        
        count = [0] * n
        merge_sort(0, n - 1)
        return count
        
            
            