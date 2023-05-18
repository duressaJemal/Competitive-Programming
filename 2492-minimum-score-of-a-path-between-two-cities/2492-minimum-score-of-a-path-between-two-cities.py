# Time: O(V + E)
# Space: O(V)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        def find(node):
            
            p = node
            while node != parent[node]:
                node = parent[node]
            while p != node:
                cur_parent = parent[p]
                parent[p] = node
                p = cur_parent
            return node
            
            
        def union(node1, node2, distance):
            
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            if p_node1 == p_node2:
                return
            
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1

            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
        
            if rank[p_node1] == rank[p_node2]:
                parent[p_node2] = p_node1
                rank[p_node1] += 1
                
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        answer = float("inf")
        
        for node1, node2, distance in roads:
            union(node1, node2, distance)
        
        
        for node1, node2, distance in roads:
            if find(1) == find(node1):
                answer = min(answer, distance)
                
        return answer
        

        
        
        