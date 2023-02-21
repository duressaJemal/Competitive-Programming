class Node:
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.dummy = Node()
        self.dummy.next = self.head
    
        
    def get(self, index: int) -> int:
        
        current = self.dummy.next
        if not current:
            return -1
        
        count = 0
        
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next
            
        return -1

    def addAtHead(self, val: int) -> None:
        
        current = self.dummy
        temp = current.next
        node = Node(val)
        current.next = node
        node.next = temp

            
    def addAtTail(self, val: int) -> None:
        
        current = self.dummy
        while current and current.next:
            current = current.next
        
        node = Node(val)
        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
   
        current = self.dummy
        count = 0
        
        while current:
            if count == index:
                temp = current.next
                node = Node(val)
                current.next = node
                node.next = temp
             
            current = current.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        
        current = self.dummy
        count = 0
        
        while current and current.next:
            if count == index:
                current.next = current.next.next
                break
            current = current.next
            count += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)