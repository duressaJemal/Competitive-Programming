# Time: O(N + M), where N = len(s) and M = len(shifts)
# Space: O(N)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        prefix = [0] * (n + 1)
        
        for start, end, dirc in shifts:
            if dirc:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
            
        # prefix
        for index in range(1, n):
            prefix[index] += prefix[index - 1]
        
        for index in range(n):
            # python is handling the negative ofset
            val = (ord(s[index]) - ord("a") + prefix[index]) % 26 
            prefix[index] = chr(ord("a") + val)
        
        prefix.pop() # remove the extra char
        return "".join(prefix)