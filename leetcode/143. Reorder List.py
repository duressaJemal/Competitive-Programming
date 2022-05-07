# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow , fast = head, head
        counter = 0
        # finding the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            counter += 1
        
        current = slow.next
        slow.next = None
        prev = None
        
        # reverse the second half of the list
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        if prev == None:
            return head
        
        current = head
        # stich together the left and right linked list
        while current.next and prev.next:
            
            temp = current.next
            temp2 = prev.next
            
            current.next = prev
            current = current.next
            current.next = temp
            current = current.next
            prev = temp2

        if current.next == None:
            current.next = prev
            
        elif prev.next == None:
            temp = current.next
            current.next = prev
            current = current.next
            current.next = temp
        
        return head
