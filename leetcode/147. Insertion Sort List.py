# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy_head = dummy
        
        current = head
        while current:

            temp = current.next
            dummy_head = self.insertNode(dummy_head, current)
            current = temp

        return dummy_head.next
        
    def insertNode(self, dummy_head, node):
        
        if not dummy_head.next:
            dummy_head.next = node
            node.next = None
            return dummy_head
        
        current = dummy_head
        
        flag = True
        while current.next:
            if current.next.val > node.val:
                temp = current.next
                current.next = node
                node.next = temp
                flag = False
                break
            current = current.next

        if flag:
            current.next = node
            node.next = None
            
        return dummy_head
