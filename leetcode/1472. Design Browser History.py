#link: https://leetcode.com/problems/design-browser-history/

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_node = Node(homepage)
        

    def visit(self, url: str) -> None:
        
        current = self.current_node
        current.next = Node(url)
        current = current.next
        current.prev = self.current_node
        self.current_node = current
        
        
        
    def back(self, steps: int) -> str:
        
        current = self.current_node
        counter = steps
        
        while current.prev and steps:
            current = current.prev
            self.current_node = current
            steps -= 1
        
        return current.value
            
        
            
    def forward(self, steps: int) -> str:
        
        current = self.current_node
        counter = steps
        
        while current.next and steps:
            current = current.next
            self.current_node = current
            steps -= 1
            
        return current.value
        
        
