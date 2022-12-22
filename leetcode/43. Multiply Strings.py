# Link: https://leetcode.com/problems/multiply-strings/
#Q: 43. Multiply Strings

# Time: O(M + N) where M = len(num1), N = len(num2)
# Space: O(1)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        convert_to_int = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        
        n1 = 0
        for i in range(len(num1)):
            n1 = n1 * 10 + convert_to_int[num1[i]]
        
        n2 = 0
        for i in range(len(num2)):
            n2 = n2 * 10 + convert_to_int[num2[i]]
        
        return str(n1 * n2)
