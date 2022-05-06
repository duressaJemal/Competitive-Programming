# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        current = head
        container = []
        stack = []
        counter = {}
        
        while current:
            container.append(current.val)
            current = current.next
        
        for index, value in enumerate(container):
            while stack and value > stack[-1][0]:
                counter[stack.pop()] = value
            stack.append((value, index))
        
        output = [0] * len(container)
        
        for key in counter:
            output[key[1]] = counter[key]
        
        return output
