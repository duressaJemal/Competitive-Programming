# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(N)
# Space: O(1)

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         current = head
        
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
        
#         return head

# Time: O(N)
# Space: O(N)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head and head.next:
            
            head.next = self.deleteDuplicates(head.next)
            if head.val == head.next.val:
                return head.next
            else:
                return head
            
        return head
        
        
        
        
        
        
        
        
        