# Time: O(N)
# Space: O(N)

class StockSpanner:

    def __init__(self):
        
        self.stock = []
        
    def next(self, price: int) -> int:
        
        prev = 0
        
        if self.stock:
            prev = self.stock[-1][1]
        
        while self.stock and self.stock[-1][0] <= price:
            self.stock.pop()
        
        self.stock.append((price, prev + 1))
        
        prev = 0
        if len(self.stock) > 1:
            prev = self.stock[-2][1]
        
        return self.stock[-1][1] - prev

# Oficial Solution

# Time: O(1) - Amortized
# Space: O(N)

class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        
        ans = 1
        
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append((price, ans))
        
        return self.stack[-1][1]
        
        

            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)