# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        maintain even and odd heads
        if current node is odd index:
            link to odd nodex
        else:
            link to even nodes
        
        link tail of odd nodes to head of even nodes
        
        
        """
        
        odd_head = ListNode()
        even_head = ListNode()
        
        odd_current = odd_head
        even_current = even_head
        
        count = 1
        current = head
        
        while current:
            if count % 2 == 0:
                even_current.next = current
                current = current.next
                even_current = even_current.next
                even_current.next = None
            else:
                odd_current.next = current
                current = current.next
                odd_current = odd_current.next
                odd_current.next = None
            
            count += 1
        
        if odd_head.next:
            head1 = odd_head.next
            head2 = even_head.next
            odd_current.next = head2
            return head1
        else:
            return odd_head.next
        
        
        
        
        
        
        
        