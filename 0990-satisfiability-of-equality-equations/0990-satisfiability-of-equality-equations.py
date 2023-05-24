class DisjointUnion:
    
    def __init__(self, size = None):
        self.parents = defaultdict(lambda: '', {chr(i): chr(i) for i in range(ord('a'), ord('z')+1)})
        self.size = defaultdict(lambda : 1)
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if y_root > x_root:
            x_root, y_root = y_root, x_root
        
        self.parents[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        dsu = DisjointUnion()
        repel = defaultdict(set)
        
        for equ in equations:
            x = equ[0]
            y = equ[3]
            equality = equ[1]
            
            if equality == "=":
                dsu.union(x, y)
            
        
        for equ in equations:
            x = equ[0]
            y = equ[3]
            equality = equ[1]
            
            if equality == "!":
                x_root = dsu.find(x)
                y_root = dsu.find(y)
                
                if x_root == y_root:
                    return False
                
            
        return True
        
        

    
    
    