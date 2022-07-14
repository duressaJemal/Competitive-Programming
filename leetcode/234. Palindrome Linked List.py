# link: https://leetcode.com/problems/palindrome-linked-list/submissions/

# Naive

# time: O(n)
# space: O(n)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        container = []
        current = head
        while current:
            container.append(current.val)
            current = current.next
        start = 0
        end = len(container) - 1
        while end >= start:
            if container[end] != container[start]:
                return False
            start += 1
            end -= 1
        return True


# Follow-up

# time: O(n)
# space: O(1)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        current = head
        count = count // 2
        while count > 0:
            current = current.next
            count -= 1
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # head1 ---- head
        # head2 ---- prev
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head  =head.next
        
        return True
        
        
            
        
        
        
            
          
