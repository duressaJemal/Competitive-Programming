# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(node, count):
            
            prev = None
            while count <= right:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
                count += 1
            
            return prev, node
            
            
        
        dummy = ListNode()
        dummy.next = head
        
        count = 1
        cur = dummy
        
        # find the starting node
        while count < left:
            cur = cur.next
            count += 1
        
        start, end = reverse(cur.next, count)
        
        cur.next.next = end 
        cur.next = start
        
        return dummy.next
        
        
        
        