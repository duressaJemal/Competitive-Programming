# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        order = []
        cur = head
        
        while cur:
            order.append(cur)
            cur = cur.next
        
        for index in range(len(order) - 1, -1, -1):
            
            value = order[index]
            
            while value and value.next:
                if value.val >= value.next.val:
                    value.val, value.next.val = value.next.val, value.val
                    # adjust
                    value = value.next
                else:
                    break
        return head
    
    
    
    
    
    
    
        