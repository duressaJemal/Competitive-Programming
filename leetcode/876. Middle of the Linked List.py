# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        counter = 1
        
        while current.next != None:
            counter += 1
            current = current.next
        
        current = head
        
        for i in range(counter//2):
            current = current.next
            
        return current
