# Link: https://leetcode.com/problems/merge-sorted-array/
#Q: 88. Merge Sorted Array

# Time: O(M + N)
# Space: O(M)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if not m and n:
            
            for i in range(n):
                nums1[i] = nums2[i]
                
        elif m and n:
            
            n1 = nums1[:m]
            current_index = 0

            i, j = 0, 0
            while i < m or j < n:
                if i < m and j < n:
                    if n1[i] <= nums2[j]:
                        nums1[current_index] = n1[i]
                        current_index += 1
                        i += 1
                    else:
                        nums1[current_index] = nums2[j]
                        current_index += 1
                        j += 1
                elif i < m:
                    while i < m:
                        nums1[current_index] = n1[i]
                        current_index += 1
                        i += 1
                else:
                    while j < n:
                        nums1[current_index] = nums2[j]
                        current_index += 1
                        j += 1


# From discuss section
# Time: O(M + N)
# Space: O(N)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
                
        if n > 0:
            nums1[:n] = nums2[:n]
        
            
            
            
            
            
                
