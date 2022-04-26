class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        counter, add = 0, 0
        holder, unique = [], set()
        
        for num in nums:
            
            if num in unique:
                add = holder[-1] - num + 1
                num += add
                counter += add
                
            unique.add(num)
            holder.append(num)
                
        return counter
