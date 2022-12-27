# Link: https://leetcode.com/problems/find-duplicate-file-in-system/
#Q: 609. Find Duplicate File in System

# Time: O(M * N) where M = average len paths
# Space: O(M * N)

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        output = []
        count = defaultdict(list)
        
        for string in paths:
            string = string.split()
            root = string[0]
            
            for i in range(1, len(string)):
                file, content = string[i].split("(")
                count[content[:-1]].append(root + "/" + file)
        
        for key in count:
            if len(count[key]) > 1:
                output.append(count[key])
        
        return output
            
            
            
            
            
