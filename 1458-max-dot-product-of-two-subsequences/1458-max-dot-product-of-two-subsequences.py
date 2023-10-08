class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        l_1 = len(nums1)
        l_2 = len(nums2)
        
        @cache
        def dp(index_1, index_2):

            if index_1 >= l_1 or index_2 >= l_2:
                return 0
            
            take_take = (nums1[index_1] * nums2[index_2]) + dp(index_1 + 1, index_2 + 1)
            take_skip = dp(index_1, index_2 + 1)
            not_take = dp(index_1 + 1, index_2)
            
            return max(take_take, take_skip, not_take)
        
        output = dp(0, 0)
        if not output:
            
            if 0 in nums1 or 0 in nums2:
                return output
            else:
                
                pos_1 = min(nums1) * max(nums2)
                pos_2 = min(nums2) * max(nums1)
                
                return max(pos_1, pos_2)
            
        return output

            
            