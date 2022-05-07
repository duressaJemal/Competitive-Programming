# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy
        
        slow, fast = head, head
        
        if not head:
            return head
        
        while fast and fast.next:
            
            while fast.next and slow.val == fast.next.val:
                fast = fast.next
                
            if fast == slow:
                dummy.next = fast
                dummy = dummy.next
                slow = fast.next
                fast = fast.next
                dummy.next = None
                
            else:
                slow = fast.next
                fast = fast.next
            
        dummy.next = fast
        
        return current.next
