class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        l_1 = len(nums1)
        l_2 = len(nums2)
        
        @cache
        def dp(index_1, index_2):
            
            if index_1 >= l_1:
                return 0
            
            if index_2 >= l_2:
                return 0
            
            # take
            
            take_from_second = (nums1[index_1] * nums2[index_2]) + dp(index_1 + 1, index_2 + 1)
            skip_second = dp(index_1, index_2 + 1)
            
            take = max(take_from_second, skip_second)
            
            
            # not take
            not_take = dp(index_1 + 1, index_2)
            
            return max(take, not_take)
        
        output = dp(0, 0)
        if not output:
            if 0 in nums1 or 0 in nums2:
                return output
            else:
            
                mn = float("inf")
                mx = float("-inf")
                
                if nums1[0] < 0:
                    mn = max(nums1)
                    mx = min(nums2)
                else:
                    mn = max(nums2)
                    mx = min(nums1)
                
                return mn * mx
            
        return output

            
            