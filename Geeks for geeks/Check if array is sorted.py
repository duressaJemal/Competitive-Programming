#User function Template for python3

# Time: O(N)
# Space: O(1)

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for index in range(1, n):
            if arr[index - 1] > arr[index]:
                return False
        
        return True
