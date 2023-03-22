# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(N)
# Space: O(1)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # adjust
        current = slow
        
        prev = None
        while current:
            
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        mx = 0
        # compare

        while prev:
            mx = max(mx, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        return mx
        
        
        
        
        