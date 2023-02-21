# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(N)
# Space: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(current):
            
            prev = None
            
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            return prev
        
        
        # count total nodes
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        
        # reverse half of the linked list
        current = head
        count = count // 2
        
        while count:
            current = current.next
            count -= 1
        
        # reverse the second half
        head2 = reverse(current)
        
        # check for palindrome
        while head and head2:
            if head.val != head2.val:
                return False
            else:
                head = head.next
                head2 = head2.next
                
        return True
        
        
            
        
        
        
        
        