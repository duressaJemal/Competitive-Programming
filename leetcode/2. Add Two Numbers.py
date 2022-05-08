# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() # creation of dummy node
        head = dummy
        leftover = 0
        
        def add(node, value):
            """
            Adds sum values to given node and also keeps track of the leftover"""
            
            if value > 9:
                a = value % 10
                leftover = value // 10
                node.val = a
                
            else:
                node.val = value
                leftover = 0
                
            return leftover
        
        while l1 and l2:
            
            addition = l1.val + l2.val + leftover
            leftover = add(l1, addition)
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
            
        if not l1: # to change if l1 become empty 
            l1 = l2
        
        while l1: # changes the val of nodes until the node become None
            
            addition = l1.val + leftover
            leftover = add(l1, addition)
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        
        if leftover != 0: # handles leftover if no node to store value to.
            dummy.next = ListNode(leftover)
        
        return head.next
        
            
