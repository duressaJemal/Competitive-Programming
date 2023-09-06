# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def split(head, step):
    
            temp_head = head
            while head:
                
                if step == 1:
                    temp = head.next
                    head.next = None
                    output.append(temp_head)
                    head = temp
                    break
                else:
                    head = head.next
                    step -= 1
            
            return head
            
        output = []
        
        # count the length of the linked list
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
            
        
        # to split appropriatly
        while count:
            cur = ceil(count / k)
            count -= cur
            k -= 1
            head = split(head, cur)
            
        # egde case
        while k:
            output.append(None)
            k -= 1
            
        return output
                
                
            
            
            
            
        