class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        output = []
        for num in nums1:
            
            number_index = indexOf(nums2, num)
            n = len(nums2)
            
            for i in range(number_index, n):
                
                if nums2[i] > nums2[number_index]:
                    output.append(nums2[i])
                    result = "found"
                    break

                if i == len(nums2) - 1:
                    output.append(-1)
                
        return output
