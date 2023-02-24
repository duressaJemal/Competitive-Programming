class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [-1] * self.size
        self.count = 0
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        
        if self.count == self.size:
            return False
        
        self.queue[self.end] = value
        self.end = (self.end + 1) % self.size # insertion index
        self.count += 1
        
        return True
         
    def deQueue(self) -> bool:
        
        if self.queue[self.start] == -1:
            return False
        
        self.queue[self.start] = -1
        self.start = (self.start + 1) % self.size # next element
        self.count -= 1
        return True
        
    def Front(self) -> int:
        
        return self.queue[self.start]
    
    def Rear(self) -> int:
        
        return self.queue[(self.end - 1) % self.size]
        
    def isEmpty(self) -> bool:
        
        return self.count == 0
        
    def isFull(self) -> bool:
        
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()