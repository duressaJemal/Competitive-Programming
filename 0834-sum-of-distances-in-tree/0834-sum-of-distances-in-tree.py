class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # find the parent node:
        parent = None
        for node in graph:
            if len(graph[node]) == 1:
                parent = node
                break
                
        if parent == None:
            parent = 0
        
        # count nodes in subarray of each node
        def count_nodes(root, parent):
            
            visited.add(root)
            count = 1
            for child in graph[root]:
                if child not in visited:
                    count += count_nodes(child, root)
            count_map[root] = n - count #(parent_node, count of nodes in subtree)
            return count
        
        def find_distance(root, count):
            
            visited.add(root)
            res[0] += count
            
            for child in graph[root]:
                if child not in visited:
                    find_distance(child, count + 1)
            return
        
        def count(root, parent, parent_value):
            
            visited.add(root)
            increment = count_map[root] - 1
            decrement = n - count_map[root] - 1
            
#             print("node", root)
#             print("increment", increment)
#             print("decrement", decrement)
            
            cur = parent_value + increment - decrement
            # print("final value", cur)
            output[root] = cur
            
            for child in graph[root]:
                if child not in visited:
                    count(child, root, cur)
            
            return
            
            
        visited = set()
        count_map = {}
        count_nodes(parent, -1)
        
        output = [0] * n
        res = [0]
        visited = set()
        find_distance(parent, 0) # find the distance from parent to all node
        output[parent] = res[0]
        
        visited = {parent}
        for child in graph[parent]:
            if child not in visited:
                count(child, parent, output[parent])
            
        return output
        

        
        
        