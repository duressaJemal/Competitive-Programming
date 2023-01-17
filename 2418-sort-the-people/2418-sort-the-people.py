# Bubble sort

# Time: O(N^2)
# Space: O(1)

# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         n = len(names)
    
#         # sort using bubble sort
#         for iteration in range(n):
#             for index in range(1, n - iteration):
#                 if heights[index] > heights[index - 1]:
#                     heights[index], heights[index - 1] = heights[index - 1], heights[index]
#                     names[index], names[index - 1] = names[index - 1], names[index]
                
#         return names

# Selection sort

# Time: O(N^2)
# Space: O(1)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        def search_minimum(start, end):
            
            minimum_value = heights[start]
            minimum_index = start
            
            while start <= end:
                if heights[start] < minimum_value:
                    minimum_value = heights[start]
                    minimum_index = start
                start += 1
            
            return minimum_index
        
        n = len(names)
        current_index = n - 1
        
        while current_index >= 0:
            
            minimum_index = search_minimum(0, current_index)
            heights[minimum_index], heights[current_index] = heights[current_index], heights[minimum_index]
            names[minimum_index], names[current_index] = names[current_index], names[minimum_index]
            current_index -= 1
            
        return names
                
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

