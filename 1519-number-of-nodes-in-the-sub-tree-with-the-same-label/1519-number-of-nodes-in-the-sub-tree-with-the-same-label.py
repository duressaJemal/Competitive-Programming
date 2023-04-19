# Time: O(N)
# Space: O(H)

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        def postorder(node):
            visited.add(node)
            counter = [0] * 26
            
            for child in graph[node]:
                if child not in visited:
                    cur = postorder(child)
                    for index in range(26):
                        counter[index] += cur[index]
                        
            
            # increment the total count of labels
            current_label = labels[node]
            current_index = ord(current_label) - ord("a")
            counter[current_index] += 1
            
            # record
            output[node] = counter[current_index]
            
            return counter
    
        # build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        output = [0] * n
        visited = set()
        
        postorder(0)
        
        return output
        