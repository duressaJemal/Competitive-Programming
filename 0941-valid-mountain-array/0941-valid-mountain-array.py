# optimized

# Time: O(N)
# Space: O(1)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        
        increasing_index = 0
        decreasing_index = n - 1
        
        for index in range(1, n):
            if arr[index] - arr[index - 1] > 0:
                increasing_index += 1
            else:
                break
        
        for index in range(n - 1, 0, - 1):
            if arr[index - 1] > arr[index]:
                decreasing_index -= 1
            else:
                break
        
        return 0 < increasing_index == decreasing_index < n - 1
        
            
# Time: O(N)
# Space: O(N)

# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
        
#         n = len(arr)
#         if n < 3:
#             return False
        
#         difference = []
        
#         for index in range(1, n):
#             difference.append(arr[index] - arr[index - 1])
        
#         if difference[0] <= 0:
#             return False
        
#         count = 0
#         for index in range(1, len(difference)):
#             if difference[index]:
#                 if difference[index] * difference[index - 1] < 0:
#                     count += 1
#             else:
#                 return False

#         return count == 1
    
    
    
    
        
        
        