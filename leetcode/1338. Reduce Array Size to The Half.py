class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        d = {}
        
        for i in arr:
            
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        ordered = sorted(d.items(), key = lambda kv: (kv[1]), reverse = True)

        sum = 0
        output = 0
        
        for i in range(len(ordered)):
  
            if sum < len(arr)//2:
                sum += ordered[i][1]
                output += 1

        return output
            
