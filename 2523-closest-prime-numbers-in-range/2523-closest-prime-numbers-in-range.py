# Time: O(N*(log(N)) ^ 2)
# Space: O(N ^ 0.5)

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def find_all_primes(end):
            for index in range(2, end + 1):
                cur = index
                
                if is_prime[cur]:
                    while cur <= right:
                        is_prime[cur] = False
                        cur += index
                    is_prime[index] = True
                
        mx = right
        is_prime = [True for _ in range(mx + 1)]
        is_prime[0] = False
        is_prime[1] = False
        
        end = ceil(sqrt(mx)) # optimized sieve
        find_all_primes(end)
        
        res = []
        for val in range(left, right + 1):
            if is_prime[val]:
                res.append(val)

        # record prime pairs and thier gaps
        distance = [float("inf"), [0, 0]]
        if len(res) > 1:
            for index in range(1, len(res)):
                distance = min(distance, [(res[index] - res[index - 1]), [res[index - 1], res[index]]]) 
        else:
            return [-1, -1]
        
        return [distance[1][0], distance[1][1]]                       
        
                               
                               
        
        
        
        
        
        
            
            
            