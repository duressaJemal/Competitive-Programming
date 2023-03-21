# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        count = 1
        current = dummy
        
        while current:
            
            if count == left:
                
                # reverse
                prev = None
                cur = current.next
                rev_tail = cur
                
                while count != right + 1:
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    count += 1
                
                current.next = prev
                rev_tail.next = cur
                
                break
                
            else:
                count += 1
                current = current.next
            
            
        return dummy.next