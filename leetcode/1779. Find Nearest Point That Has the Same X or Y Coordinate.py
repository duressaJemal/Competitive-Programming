# Link: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
#Q: 1779. Find Nearest Point That Has the Same X or Y Coordinate

# Time: O(N)
# Space: O(1)

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        output = [float("inf"), 0]
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                man_d = abs(x - point[0]) + abs(y - point[1])
                if man_d < output[0]:
                    output = [man_d, index]
        
        return output[1] if output[0] != float("inf") else -1

    
    
    
    
