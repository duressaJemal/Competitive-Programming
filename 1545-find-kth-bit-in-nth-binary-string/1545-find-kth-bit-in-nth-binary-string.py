class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(string):
            res = []
            for chr in string:
                if chr == "0":
                    res.append("1")
                else:
                    res.append("0")
                    
            return "".join(res)
        
        def solve(index):
            
            # base case
            if index == 1:
                return "0"
            
            sub = solve(index - 1)
            return sub + "1" + invert(sub)[::-1]
        
        return solve(n)[k - 1]
        
            
            
            