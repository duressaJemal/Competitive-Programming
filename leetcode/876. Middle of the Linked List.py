# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast, slow = head, head
        
        while fast:
            
            if fast.next == None:
                return slow
            
            elif fast.next and fast.next.next == None:
                return slow.next
            
            else:
                
                fast = fast.next.next
                slow = slow.next
            
