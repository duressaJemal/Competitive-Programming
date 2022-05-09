# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        current = head
        
        while current:
            
            while current.next and current.val == val:

                current = current.next
                continue
            
            if current.val == val and current.next == None:
                prev.next = None
                return dummy.next
            
            prev.next = current
            prev = prev.next
            current = current.next
        
        return dummy.next
