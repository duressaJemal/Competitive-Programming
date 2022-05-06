class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.dummy = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index > self.length:
            return -1
        
        current = self.dummy.next
        for i in range(index):
            current = current.next
        
        if current == None:
            return  -1
        return current.val
        

    def addAtHead(self, val: int) -> None:
        
        current = self.dummy.next
        self.dummy.next = ListNode(val)
        self.dummy.next.next = current
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        
        current = self.dummy.next
        
        if current == None:
            self.dummy.next = ListNode(val)
            return
        
        while current.next:
            current = current.next
        
        current.next = ListNode(val)
        self.length += 1
        return
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index < 0 or index > self.length:
            return 
        
        current = self.dummy.next
        
        if index == 0:
            self.dummy.next = ListNode(val)
            self.dummy.next.next = current
        else:
            
            for i in range(index-1):
                current = current.next
            
            temp = current.next
            current.next = ListNode(val)
            current.next.next = temp
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index > self.length:
            return 
        
        current = self.dummy.next
        
        if index == 0:
            self.dummy.next = self.dummy.next.next
        else:
            for i in range(index-1):
                current = current.next
            
            if current.next == None:
                return
            
            current.next = current.next.next
        self.length -= 1
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
