class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        if n < 3:
            return False
        
        difference = []
        
        for index in range(1, n):
            difference.append(arr[index] - arr[index - 1])
        
        if difference[0] <= 0:
            return False
        
        count = 0
        for index in range(1, len(difference)):
            if difference[index]:
                if difference[index] * difference[index - 1] < 0:
                    count += 1
            else:
                return False

        return count == 1
    
        
        
        