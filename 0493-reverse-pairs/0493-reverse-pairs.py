class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        
        def merge(left, right):
            
            """
            Merge two sorted arrays into sorted array
            
            """
            
            
            # count all valid pairs
            count = 0
            for val in left:
                count += bisect_left(right, ceil(val / 2))
            
            res[0] += count
                
            
            left_index = 0
            right_index = 0
            
            combined = [0] * (len(left) + len(right))
            
            prev = 0
            count = 0 
            
            while left_index < len(left) or right_index < len(right):

                # condition to choose the left value
                if right_index >= len(right) or (left_index < len(left) and left[left_index] <= right[right_index]):
                    # record valid pairs and adjust previous count
#                     res[0] += (prev + count)
#                     # print(prev, count, left[left_index])
#                     prev = count
#                     count = 0
                    
                    # merge
                    combined[left_index + right_index] = left[left_index]
                    left_index += 1
                    
                else:
                    # right value is less than the left value
                    if left_index < len(left) and left[left_index] > right[right_index] * 2:
                        count += 1
#                         print(left[left_index], "left")
#                         print(right[right_index], "right")

#                         print("yaaa")
                    
                    # merge
                    combined[left_index + right_index] = right[right_index]
                    right_index += 1
                    
            return combined
                    
        def merge_sort(l, r):
            
            if l == r:
                return [nums[l]]
            
            mid = l + (r - l) // 2
            
            merge_left = merge_sort(l, mid)
            merge_right = merge_sort(mid + 1, r)
            
            merged_array = merge(merge_left, merge_right)
            
            return merged_array
        
        res = [0]
        merge_sort(0, len(nums) - 1)
        return res[0]
        
        