class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        
        for i in range(len(l)):
              output.append(self.checker(nums[ l[i]:r[i] + 1 ]))
        return output
        
    def checker(self, num):
        print(num)
        
        num.sort()
        for i in range(len(num)):
            if len(num) == 2:
                return True
            if i + 1 == len(num) or i + 2 == len(num):
                break
            if num[i] - num[i+1] != num[i+1] - num[i+2]:
                return False
        return True
