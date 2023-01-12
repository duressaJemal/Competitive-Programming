class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        
        for index in range(n // 2):
            
            right_index = n - (index + 1)
            s[index], s[right_index] = s[right_index], s[index]
        