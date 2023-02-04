# Time: O(Nlog(N))
# Space: O(1)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        n = len(people)
        count = 0
        
        people.sort()
        
        left = 0
        right = n - 1
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1
        
        return count
            
        