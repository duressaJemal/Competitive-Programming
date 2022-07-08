# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Naive

# time: O(m), m : the lentgh of the linked list
# space: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        remove = count - n
        if not remove:
            head = head.next
            return head
        current = head
        remove -= 1
        while remove:
            current = current.next
            remove -= 1
        current.next = current.next.next
        return head
    
    

# Two pointer

# time: O(n) (only one pass)
# space: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow, fast = head, head
        
        for _ in range(n):
            fast  = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        
            
        
        
