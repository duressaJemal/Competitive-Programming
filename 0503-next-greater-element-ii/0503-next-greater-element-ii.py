class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [-1] * (n)
        greater = []
        hash_map = defaultdict(lambda : -1)
        
        finished = False
        
        for index in range(2 * n):
            
            current_index = index % n
            value = nums[current_index]
            
            while greater and value >= greater[-1][1]:
                if value == greater[-1][1] and current_index == greater[-1][0]:
                    finished = True
                    break
                if value > greater[-1][1]:
                    hash_map[greater.pop()[0]] = value
                else:
                    break
            
            if not finished:
                greater.append((current_index, value))
            else:
                break
        
        
        for key in hash_map:
            result[key] = hash_map[key]
        
        return result
            
            
            
            
        
        
    