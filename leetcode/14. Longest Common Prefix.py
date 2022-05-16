#link https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        output = []
        
        for i in range(len(strs[0])):
            first = strs[0][i]
            
            for j in range(len(strs)):

                if i >= len(strs[j]) or strs[j][i] != first:
                    return "".join(output)
                
            output.append(strs[j][i])
    
        return "".join(output)
