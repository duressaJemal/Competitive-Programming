# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time: O(N)
# Space: O(1)

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         # phase 1
#         fast = head
#         slow = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
            
#             if slow == fast:
#                 return True
        
#         return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()
        
        while head:
            if head in visited:
                return True
            
            visited.add(head)
            head = head.next
        
        return False
        