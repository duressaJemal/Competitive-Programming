# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        current = dummy
        
        while current and current.next and current.next.next:
            if current.next.val == current.next.next.val:
                duplicate = current.next.val
                
                # find next non duplicate value
                temp = current.next
                while temp and temp.val == duplicate:
                    temp = temp.next
                
                current.next = temp
            else:
                current = current.next
        
        return dummy.next
                