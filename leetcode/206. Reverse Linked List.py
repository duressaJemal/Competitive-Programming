# link: https://leetcode.com/problems/reverse-linked-list/submissions/

# Iterative

# time: O(n)
# space: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        prev = None
        current = head
        while current:
            temporary = current.next
            current.next = prev
            prev = current
            current = temporary
        return prev
    
# Recursive

# time: O(n)
# space: (n)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(current, prev=None):
            if not current:
                return prev
            tempo = current.next
            current.next = prev
            return helper(tempo, current)
        
        return helper(head)
            

            
