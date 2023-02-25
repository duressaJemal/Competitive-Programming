# Time: O(N + M) where N = len(nums1), M = len(nums2)
# Space: O(N)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = [float("inf")]
        output = []
        
        hash_map = defaultdict(lambda: - 1)
        
        # build monotonic
        for value in nums2:
            while value > stack[-1]:
                hash_map[stack.pop()] = value
            stack.append(value)
        
        for val in nums1:
            output.append(hash_map[val])
        
        return output
        
            
        
        
        