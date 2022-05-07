# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        container = []
        current = head
        
        while current:
            
            container.append(current.val)
            current = current.next
            
        start = 0
        end = len(container) - 1
        
        while end >= start:
            
            if container[end] != container[start]:
                return False
            start += 1
            end -= 1
            
        return True
            
            
