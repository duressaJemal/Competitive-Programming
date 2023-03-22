# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(N)
# Space: O(1)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add(cur):
            r = cur // 10
            cur = cur % 10
            
            return r, cur
        
        dummy = ListNode()
        current = dummy
        
        r = 0
        while l1 and l2:
            
            cur = l1.val + l2.val + r
            r, cur = add(cur)
            l1.val = cur
            current.next = l1
            # adjust
            current = current.next
            
            l1 = l1.next
            l2 = l2.next
            
        if l1 or l2:
        
            if l2:
                current.next = l2
                current = current.next
            elif l1:
                current.next = l1
                current = current.next

            while current:

                cur = current.val + r
                r, cur = add(cur)

                current.val = cur
                if current.next:
                    current = current.next
                else:
                    break

        if r:
            node = ListNode(r)
            current.next = node

        return dummy.next













