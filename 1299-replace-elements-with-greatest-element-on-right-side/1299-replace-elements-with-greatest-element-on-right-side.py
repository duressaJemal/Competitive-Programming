# Time: O(N)
# Space: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        max_to_right = -1
        
        for index in range(n - 1, - 1, -1):
            arr[index], max_to_right = max_to_right, max(arr[index], max_to_right)
        
        return arr
        
        
        
        