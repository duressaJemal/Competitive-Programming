class MyQueue:

    def __init__(self):
        self.container = []
        
    def push(self, x: int) -> None:
        self.container.append(x)

    def pop(self) -> int:
        return self.container.pop(0)

    def peek(self) -> int:
        return self.container[0]

    def empty(self) -> bool:
        if len(self.container) == 0:
            return True
        return False
