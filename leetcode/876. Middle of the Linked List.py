# link: https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# time: O(n)
# space: O(1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        slow, fast, = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
