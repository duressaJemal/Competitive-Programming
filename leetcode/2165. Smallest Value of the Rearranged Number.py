#link https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution:
    def smallestNumber(self, num: int) -> int:
        
        s = str(num)
        s = list(s)
        s.sort()
        
        if num < 0:
            s = s[1:]
            s.sort(reverse = True)
            output = "".join(s)
            return 0 - int(output)
                
        else:
            counter = 0
            for num in s:
                if num == "0":
                    counter += 1
            
            if counter < len(s):
                output = [s[counter]] + (["0"] * counter) + s[counter + 1:]
                return int("".join(output))
            else:
                return 0
            
            
            
