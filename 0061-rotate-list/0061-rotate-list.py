# Time: O()

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        # count total number on nodes
        count = 0
        current = head
        tail = head
        
        while current:
            count += 1
            current = current.next
        
        shift = k % count
        if not shift:
            return head
        
        cur = head
        n = 1
        while n < count - shift:
            n += 1
            cur = cur.next
        
        rev_head = cur.next
        cur.next = None
        
        cur = rev_head
        while cur.next:
            cur = cur.next
        
        cur.next = head
        return rev_head
        
        
        
        
        
        
        
        
        
        
    
            
        
        
        