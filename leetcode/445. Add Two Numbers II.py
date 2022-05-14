#link 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        current = l1
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        l1 = prev
        prev = None
        current = l2
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        l2 = prev
        dummy = ListNode()
        current = dummy
        
        def add(x):
            nonlocal current
            nonlocal l1
            nonlocal leftover
            if x > 9:
                a = x % 10
                leftover = x // 10
            else:
                a = x
                
            l1.val = a
            current.next = l1
            l1 = l1.next
            current = current.next
            return leftover
    
        leftover = 0
        while l1 and l2:
            addition = l1.val + l2.val + leftover
            leftover = 0 
            leftover = add(addition)
            l2 = l2.next
        
        
        if not l1:
            l1 = l2
              
        if l1 and leftover != 0:
              while l1:
                    
                    addition = l1.val + leftover
                    leftover = 0
                    leftover = add(addition)
        else:
              current.next = l1
              
        if leftover != 0 and not l1:
            dummy2 = ListNode(leftover)
            current.next = dummy2
    
        
        prev = None
        current = dummy.next
        
        while current:
            temp = current.next
            current.next = prev
            prev = current 
            current = temp
            
        return prev
        
        
            
                
                
            
            
            
