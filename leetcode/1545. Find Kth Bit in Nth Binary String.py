class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        output = self.s(n)
        return output[k-1]
        
    def s(self, n):
        """
        helper function to handle the recursive call made
        """

        # base case (recursion terminating case)
        if n == 1:
            return ["0"]
        
        value = self.s(n-1)
        value = value + ["1"] +  self.rev_inv(value)
        return value
    
    def rev_inv(self, value):
        """
        function to reverse and invert the list
        """
        # inverting the string values
        for i in range(len(value)):
            if value[i] == "0":
                value[i] = "1"
            else:
                value[i] = "0"
                
        # reverse the list
        value = value[::-1]
        return value
