# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        current = head
        left = head
        right = head.next
        head = right
        
        while left and right:

            temp = right.next
            current.next = right # creates connection bn previous nodes and the right node
            right.next = left # pointing the right node to the left node
            left.next = temp # pointing the left node to the right next node
            current = left # updating the current node
            
            left = left.next # updating the left node
            if not left or not left.next:
                break
            right = left.next # updating the right node

        return head
