class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        
        prefix = [0] * n
        
        for start, end, dirc in shifts:
            if dirc:
                prefix[start] += 1
                if end + 1 < n:
                    prefix[end + 1] -= 1
            
            else:
                prefix[start] -= 1
                if end + 1 < n:
                    prefix[end + 1] += 1
            
        # prefix
        for index in range(1, n):
            prefix[index] += prefix[index - 1]
        
        for index in range(n):
            val = (ord(s[index]) - ord("a") + prefix[index]) % 26
            if val >= 0:
                prefix[index] = chr(ord("a") + val)
            else:
                prefix[index] = chr(ord("z") - val)
            
        
        return "".join(prefix)