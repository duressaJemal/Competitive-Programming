# Time: O(N)
# Space: O(K)

class DataStream:

    def __init__(self, value: int, k: int):
        
        self.value = value
        self.k = k
        self.queue = deque([])
        self.dict = defaultdict(int)

    def consec(self, num: int) -> bool:
        
        # add
        self.queue.append(num)
        self.dict[num] += 1
        
        # remove
        while len(self.queue) > self.k:
            self.dict[self.queue[0]] -= 1
            self.queue.popleft()
        
        if len(self.queue) == self.k and (self.value in self.dict) and (self.dict[self.value] == self.k):
            return True
        else:
            return False
            
            
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)