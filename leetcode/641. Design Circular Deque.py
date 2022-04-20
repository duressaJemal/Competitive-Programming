class MyCircularDeque:
    
    def __init__(self, k: int):
        
        self.size = 0
        self.front = 0
        self.queue = [None] * k
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        # finds the previous index 
        front = (self.k - 1 + self.front) % self.k
        self.queue[front] = value
        self.front = front
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        
        if self.isFull():
            return False
        
        # finds the end index to append value
        end = (self.size + self.front)  %  self.k
        self.queue[end] = value
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        
        if self.isEmpty():
            return False
        
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        
        if self.isEmpty():
            return False
        
        end = (self.front + self.size - 1) % self.k
        self.queue[end] = None
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        
        if self.isEmpty():
            return -1
        
        end = (self.front + self.size - 1) % self.k
        return self.queue[end]
        
    def isEmpty(self) -> bool:
        
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        
        end = (self.front + self.size - 1) % self.k
        
        if self.size == 0:
            return False
        
        # i don't know the inputs front
        if end == (self.k - 1 + self.front) % self.k:
            return True
        return False
