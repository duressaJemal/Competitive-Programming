class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def is_valid(arr):
            
            temp = [0] * (n)
            
            for f, t in arr:
                temp[f] += 1
                temp[t] -= 1
                
            for val in temp:
                if val:
                    return False
            return True

        
        max_length = [0]
        def backtrack(arr, index):

            if index == len(requests):
                if is_valid(arr):
                    max_length[0] = max(max_length[0], len(arr))
                return
            
            # include
            arr.append(requests[index])
            backtrack(arr, index + 1)
            #exclude
            arr.pop()
            backtrack(arr, index + 1)
            
            return
        
        backtrack([], 0)
        return max_length[0]
    
    
    