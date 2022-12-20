# Link: https://leetcode.com/problems/longest-common-prefix/
#Q: 14. Longest Common Prefix

# Time: O(N)
# Space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        current = list(strs[0])
        
        for i in range(1, len(strs)):
            
            if not strs[i]:
                current = ""
                
            elif current and strs[i]:
                c_i, s_i = 0, 0
                
                while c_i < len(current) and s_i < len(strs[i]) and current[c_i] == strs[i][s_i]:
                    c_i += 1
                    s_i += 1
                
                current = "" if not c_i else current[:c_i]
                    
        return "".join(current)
