class compare(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
        lt_num = "".join(sorted(map(str, nums),  key = compare))
        
        return "0" if lt_num[0] == "0" else lt_num
        
        
        