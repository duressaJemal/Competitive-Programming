# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        prev = None
        largest = 0
        
        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        
        # reverse the second half
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        if not prev:
            return head.val + head.next.val
        
        # compare the twin elements
        while head and prev:
            
            largest = max(largest, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        return largest
