# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        counter = 1
        special = head
        
        while current.next:
            special = current
            current = current.next
            counter += 1
        
        if n==1 and head.next:
            special.next = special.next.next
            return head
        
        current = head
        for i in range(1, counter - n):
            current = current.next
        
        print("current", current)

        if current == head and n == counter:
            head = head.next
            return head
        
        current.next = current.next.next
        
        return head
    
    #MUST BE IMPROVED
