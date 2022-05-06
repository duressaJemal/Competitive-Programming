# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        while current:
            if current.next and current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    #OLD
#         if not head:  can be avoided
#             return 
        
#         if not head.next: not needed(can be handled when returning)
#             return head
        
#         current = head
        
#         while current:
            
#             if not current.next:  can be added with the next condition
#                 break
#             if current.val == current.next.val:

#not needed(because it doesnt matter what current.next.next points to it may be valid node or None. we just need to assign it)
#                 if current.next.next:  
#                     current.next = current.next.next
#                 else:
#                     current.next = None
#             else:
#                 current = current.next
            
#         return head
    
