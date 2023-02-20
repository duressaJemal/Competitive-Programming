# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cycle = False
        
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                cycle = True
                break
        
        if cycle:
            while slow != head:
                head = head.next
                slow = slow.next
                if head == slow:
                    break
            return head
                
        else:
            return None
        