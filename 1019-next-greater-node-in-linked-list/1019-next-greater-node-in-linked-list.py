# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        hash_map = {}
        stack = []
        output = []
        
        current = head
        
        while current:
            
            value = current.val
            
            while stack and stack[-1].val < value:
                hash_map[stack.pop()] = value
            stack.append(current)
            
            current = current.next
        
        current = head
        while current:
            if current in hash_map:
                output.append(hash_map[current])
            else:
                output.append(0)
            
            current = current.next
        return output
        
        
        