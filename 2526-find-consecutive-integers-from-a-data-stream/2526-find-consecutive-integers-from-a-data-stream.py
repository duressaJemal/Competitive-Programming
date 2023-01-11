class DataStream:
    
    """
    keep track of the last value that is different from value
    if the current value is different from current value:
        return False
    else:
        check the lenght bn the last wrong value and the current value
        if it is >= k then return True
        
    
    
    """

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        self.bad_index = -1
        self.current_index = -1
        

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self.current_index += 1
        
        if num != self.value:
            self.bad_index = self.current_index 
            return False
        else:
            # check the distance between current index and bad_index
            if self.current_index - self.bad_index >= self.k:
                return True
            else:
                return False
        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)