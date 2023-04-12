class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        # build graph
        graph = defaultdict(list)
        for index, value in enumerate(parent):
            graph[value].append(index)
          
        def is_valid(cur, parent):
            if cur == 0: return True
            if s[cur] != s[parent]:
                return True
            return False
        
        def dfs(node, parent):

            cur = []
            for child in graph[node]:
                cur.append(dfs(child, node))
              
            cur.append(0)
            cur.append(0)
            cur.sort()
            
            first_largest = cur[-1]
            second_largest = cur[-2]
            
            # record result's till now
            result[0] = max(result[0], first_largest + second_largest + 1)
            
            if is_valid(node, parent):
                return first_largest + 1
            else:
                return 0

    
        result = [0]
        dfs(0, -1)
        return result[0]
                
                
                
                
                
                
                
                
            
                
        
        