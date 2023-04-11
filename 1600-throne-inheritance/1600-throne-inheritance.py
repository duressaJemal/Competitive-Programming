class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.kingName = kingName
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        
        output = []
        def dfs(node):
            if node not in self.dead:
                output.append(node)
            for child in self.graph[node]:
                dfs(child)
        
        dfs(self.kingName)
        return output
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()