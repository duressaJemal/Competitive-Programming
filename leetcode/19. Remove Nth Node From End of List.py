# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
        
        
