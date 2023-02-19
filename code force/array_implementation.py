class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
    # write your code here
        self.arr = arr
        self.capacity = capacity
        self.length = length

    def insertEnd(self, value):
    # write your code here

        self.arr[self.length] = value
        self.length += 1

    def removeEnd(self):
    # write your code here
        
            
    def insertMiddle(self, index, value):
    # write your code here, you need to shift elements after insertion
        if index < self.capacity - 1
    def removeMiddle(self, index):
    # write your code here, you need to shift elements after removal

    def printArr(self):
    # write your code here