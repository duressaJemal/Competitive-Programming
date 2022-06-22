# link https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# time: O(n * m * log(n * m)
# space: O(n * m)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        container = []
        heap_values = []
        
        for element in lists:
            head = element
            while head:
                heap_values.append(head.val)
                head = head.next
                
        heap = heap_values
        heapify(heap)
    
        while heap:
            container.append(heappop(heap))
            
        if not container:
            return None
        
        head = ListNode(container[0])
        current = head
        
        for i in range(1, len(container)):
            current.next = ListNode(container[i])
            current = current.next
        
        return head
