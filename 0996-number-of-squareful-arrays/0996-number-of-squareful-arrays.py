class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
       
        
        @lru_cache(None)
        def dp(prev, tup):
            if not tup:
                return 1
            visited = set()
            ans = 0
            
            for index in range(len(tup)):
                if tup[index] not in visited:
                    curr = prev + tup[index]
                    if prev == -1 or int(curr ** 0.5) ** 2 == curr:
                        visited.add(tup[index])
                        temp = tup[:index] + tup[index + 1:]
                        ans += dp(tup[index], temp)
            return ans
        
        return dp(-1, tuple(nums))
        

        