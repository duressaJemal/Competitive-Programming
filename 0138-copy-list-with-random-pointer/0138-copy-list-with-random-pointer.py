"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dic = {}
        
        # save all nodes with the corresponding new nodes created.
        cur = head
        while cur:
            
            node = Node(cur.val)
            if cur not in dic:
                dic[cur] = node
            
            cur = cur.next
        
        cur = head
        while cur:
            
            cor_node = dic[cur]
            
            if cur.next:
                cor_node.next = dic[cur.next]
            
            if cur.random:
                cor_node.random = dic[cur.random]
            
            cur = cur.next
        
        return dic[head] if head else None
        
        