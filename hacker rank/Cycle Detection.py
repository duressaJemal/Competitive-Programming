def has_cycle(head):
    
    slow , fast = head, head
    
    while (slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0
