# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# From discuss section

# Time: O(N)
# space: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        """
        intuition for the while loop
        
        if length is even:
            then even.next == None
        if length is odd:
            then even == None
            
        """
        
        while even and even.next:
            odd.next = odd.next.next # even.next(after update)
            even.next = even.next.next # odd.next(after update)
            
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        return head



# Time: O(N)
# Space: O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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
        


        
        
        
        
        
        
        