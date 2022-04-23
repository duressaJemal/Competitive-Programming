class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left_pointer = 0
        right_pointer = len(height) - 1
        area = 0
        
        while right_pointer > left_pointer:

            area = max(area, (right_pointer - left_pointer) * min(height[right_pointer] , height[left_pointer]))
            
            if height[right_pointer] >= height[left_pointer]:
                left_pointer += 1
                
            else:
                right_pointer -= 1
            
        return area
        
