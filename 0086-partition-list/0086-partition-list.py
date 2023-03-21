# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        if not dummy.next:
            return head
        
        left = dummy
        right = head
        
        while right:
            
            if right.val < x:
                
                left_temp = left.next
                right_temp = right.next
                
                left.next = right
                left = left.next
                right.next = left_temp
                
                while left_temp.next != right:
                    left_temp = left_temp.next
                
                left_temp.next = right_temp
                right = right.next
            else:
                right = right.next
        
        return dummy.next
                
                
                
