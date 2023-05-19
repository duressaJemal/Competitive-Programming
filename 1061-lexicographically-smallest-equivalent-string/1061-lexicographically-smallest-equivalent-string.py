class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        def find(node):
            
            # root finding
            p = node
            while node != parent[node]:
                node = parent[node]
            
            # path compresion
            while node != p:
                cur_parent = parent[p]
                parent[p] = node
                p = cur_parent
            
            return node
        
        def union(node1, node2):
            
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            if p_node1 == p_node2:
                return
            
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1
                hash_map[p_node1] = min(hash_map[p_node1], hash_map[p_node2])
            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
                hash_map[p_node2] = min(hash_map[p_node1], hash_map[p_node2])
            
            else:
                parent[p_node2] = p_node1
                hash_map[p_node1] = min(hash_map[p_node1], hash_map[p_node2])
                rank[p_node1] += 1
            
        
        hash_map = defaultdict(str)
        parent = defaultdict(str)
        rank = defaultdict(int)
        
        ofset = ord("a")
        for index in range(26):
            cur = chr(index + ofset)
            hash_map[cur] = cur
            parent[cur] = cur
            
    
        output = []
        
        n = len(s1)
        for index in range(n):
            union(s1[index], s2[index])
            
        for char in baseStr:
            root = find(char)
            val = hash_map[root]
            output.append(val)
        
        return "".join(output)
            
            
            
            
            
            