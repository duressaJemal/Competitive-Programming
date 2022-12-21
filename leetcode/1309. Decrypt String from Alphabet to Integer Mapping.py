# Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
#Q: 1309. Decrypt String from Alphabet to Integer Mapping

# Time: O(N)
# Space: O(N)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        output, i = [], len(s) - 1
        while i > -1:
            if s[i] == "#":
                output.append(chr(ord("a") + int(s[i - 2:i]) - 1))
                i -= 3
            else:
                output.append(chr(ord("a") + int(s[i:i + 1]) - 1))
                i -= 1
        
        return "".join(output[::-1])
            
