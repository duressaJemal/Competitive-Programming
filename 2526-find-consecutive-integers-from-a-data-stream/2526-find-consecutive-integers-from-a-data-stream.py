# Time: O(N)
# Space: O(1)

class DataStream:

    def __init__(self, value: int, k: int):
        
        self.value = value
        self.k = k
        self.bad_position = -1
        self.current_position = -1
        
    def consec(self, num: int) -> bool:
        
        self.current_position += 1
        if num != self.value:
            self.bad_position = self.current_position
            return False
        else:
            # check the distance between current_position and bad_position
            if self.current_position - self.bad_position >= self.k:
                return True
            else:
                return False
        
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)