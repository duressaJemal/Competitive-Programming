# Time: O(V + E)
# Space: O(V)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def find(node):
            p = node
            while node != parent[node]:
                node = parent[node]
            
            while p != node:
                cur_parent = parent[p]
                parent[p] = node
                p = cur_parent
            
            return node
            
        def union(node1, node):
            
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            if p_node1 == p_node2:
                return
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1
            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
            else:
                parent[p_node2] = p_node1
                rank[p_node1] += 1
            
            
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]
        
        for node1, node2 in edges:
            union(node1, node2)

        return find(source) == find(destination)