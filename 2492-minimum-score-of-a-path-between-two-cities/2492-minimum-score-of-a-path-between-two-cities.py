class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        def find(node):
            
            p = node
            while node != parent[node]:
                node = parent[node]
            
            while p != node:
                parent[p] = node
                p = parent[p]
            
            return node
            
            
        def union(node1, node2, distance):
            
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1
                score[p_node1] = min(score[p_node1], score[p_node2], distance)
            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
                score[p_node2] = min(score[p_node2], score[p_node1], distance)
        
            if rank[p_node1] == rank[p_node2]:
                parent[p_node2] = p_node1
                rank[p_node1] += 1
                score[p_node1] = min(score[p_node1], score[p_node2], distance)
                
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        score = [float("inf") for i in range(n + 1)]
        
        for node1, node2, distance in roads:
            union(node1, node2, distance)
        
        root = find(1)
        return score[root]
        
        

        
        
        