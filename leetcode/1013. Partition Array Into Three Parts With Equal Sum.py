# Link: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
#Q: 1013. Partition Array Into Three Parts With Equal Sum

# Time: O(N^2)
# Space: O(1)

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i - 1]
            
        is_found = False
        for i in range(n - 2):
            current = arr[i]
            if (arr[-1] - arr[i]) == 2 * current:
                j = i + 1
                while j < n - 1:
                    if arr[j] - arr[i] == current:
                        is_found = True
                        break
                    j += 1
            if is_found:
                return True
        return False
     
    
# From discuss section

# Time: O(N)
# Space: O(1)

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        average, count, prefix = sum(arr) / 3, 0, 0
        n = len(arr)
        
        for i in range(n):
            prefix += arr[i]
            if prefix == average:
                count += 1
                prefix = 0
        
        return count >= 3 and sum(arr) % 3 == 
        
# TLE

# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        # n = len(arr)
        # for i in range(1, n):
        #     arr[i] += arr[i - 1]
            
#         for i in range(1, n - 1):
#             for j in range(i, n - 1):
#                 if arr[i - 1] == arr[j] - arr[i - 1] and arr[i - 1] ==        arr[-1] - arr[j]:
#                     return True
        
#         return False
