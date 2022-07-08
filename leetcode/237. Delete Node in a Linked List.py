# link: https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val, node.next.val = node.next.val, node.val
            if not node.next.next:
                node.next = node.next.next
                break
            node = node.next
