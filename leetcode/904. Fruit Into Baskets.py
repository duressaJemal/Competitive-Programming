# link: https://leetcode.com/problems/fruit-into-baskets/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start, end, longest = 0, 0, 0
        n = len(fruits)
        fruit_types = set()
        container = {}
        
        while end < n:
            
            fruit_types.add(fruits[end])
            container[fruits[end]] = 1 + container.get(fruits[end], 0)
            
            while len(fruit_types) > 2:
                container[fruits[start]] -= 1
                if container[fruits[start]] == 0:
                    fruit_types.remove(fruits[start])
                start += 1
            
            longest = max(longest, end - start + 1)
            end += 1
        
        return longest
                    
                
            
            
            
