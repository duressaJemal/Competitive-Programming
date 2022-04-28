class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        arr = list(range(1, n + 1))
        starter = 0
        return self.recursive(arr, k, starter)
    
    def recursive(self, arr, jump, starter):
        """
        Return the last value after performing series of k jumps and removal
        arr: list generated from consecutive n natural numbers
        jump: k
        starter: the index from which counting begins
        
        """
        # recursion terminating case
        if len(arr) == 1:
            return arr[0]
        
        # for finding the index to remove
        remove = (starter + jump - 1) % len(arr)
        previous = (starter + jump - 2) % len(arr)
        
        if remove < previous:
            previous -= 1

        arr.pop(remove)
        # keeping track of the index to start from 
        starter = (previous + 1) % len(arr)
        
        return True and self.recursive( arr, jump, starter)
    
        
