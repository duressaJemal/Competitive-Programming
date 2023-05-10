class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        graph = {}
        in_degree = {}
        
        for recipe in recipes:
            graph[recipe] = []
            in_degree[recipe] = 0
        
        
        for index in range(len(recipes)):
            recipe = recipes[index]
            for pre in ingredients[index]:
                if pre in graph:
                    graph[pre].append(recipe)
                
                if pre not in supplies:
                    in_degree[recipe] += 1
        
        queue = deque([])
        for recipe in recipes:
            if not in_degree[recipe]:
                queue.append(recipe)
        
        order = []
        
        while queue:
            
            l = len(queue)
            for _ in range(l):
                
                node = queue.popleft()
                order.append(node)
                
                for child in graph[node]:
                    in_degree[child] -= 1
                    if not in_degree[child]:
                        queue.append(child)
        
        return order
   
        
        