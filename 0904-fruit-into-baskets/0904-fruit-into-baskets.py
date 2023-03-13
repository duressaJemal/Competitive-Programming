# Time: O(N)
# Space: O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n = len(fruits)
        
        dic = defaultdict(int)
        res = 0
        
        left = 0
        
        for right in range(n):
            
            # add
            dic[fruits[right]] += 1
            
            while len(dic) > 2:
                # remove
                dic[fruits[left]] -= 1
                if not dic[fruits[left]]:
                    dic.pop(fruits[left])
                
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
            
            
            