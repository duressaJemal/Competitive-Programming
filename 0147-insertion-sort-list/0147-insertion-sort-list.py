# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        while current:
            
            t_head = head

            while t_head != current:
                if t_head.val > current.val:
                    t_head.val, current.val = current.val, t_head.val
                t_head = t_head.next
            current = current.next
        
        return head
    
    
    
    
        