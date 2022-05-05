class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        container = []
        counter = {}
        
        start = 0
        end = 0
        longest = 0
        
        while end < len(fruits):
            
            # if our container is full and the next number not in container
            if len(container) == 2 and fruits[end] not in container: 
                
                counter[fruits[start]] -= 1 # keeps track of counter values
                if counter[fruits[start]] == 0: # removal condition from container
                    container.remove(fruits[start])
                start += 1
                
            else:
                #expand
                if fruits[end] not in container: # avoids adding duplicate values to container
                    container.append(fruits[end])
                    
                if fruits[end] in counter: # keep track of our fruit types
                    counter[fruits[end]] += 1
                else:
                    counter[fruits[end]] = 1
                
                longest = max(longest, end-start+1) # our longest window size
                end += 1
        
        return longest
