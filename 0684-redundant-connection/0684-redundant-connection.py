# Time: O(V + E)
# Space: O(V)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(node):
            
            p = node
            while node != parent[node]:
                node = parent[node]
            
            while p != node:
                cur_parent = parent[p]
                parent[p] = node
                p = cur_parent
            
            return node
        
        def union(node1, node2):
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            if p_node1 == p_node2:
                output[0] = [node1, node2]
                return
            
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1
            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
            
            else:
                parent[p_node2] = p_node1
                rank[p_node1] += 1
            
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        output = [[]]
        
        for node1, node2 in edges:
            union(node1, node2)
        
        
        return output[0]
            