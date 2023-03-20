class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        cookies.sort(reverse = True)
        
        self.unfair = float("inf")
        bag = [0] * k
        
        def backtrack(index):
            
            if index >= len(cookies):
                self.unfair = min(self.unfair, max(bag))
                return
            
            if max(bag) >= self.unfair: # pruning
                return
            
            for pos in range(k):
                
                # add
                bag[pos] += cookies[index]
                
                backtrack(index + 1)
                
                bag[pos] -= cookies[index]
        
        backtrack(0)
        return self.unfair
            
        