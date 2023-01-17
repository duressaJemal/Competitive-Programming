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

# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         def search_minimum(start, end):
            
#             minimum = [heights[start], start] # height, index
            
#             while start <= end:
#                 if heights[start] < minimum[0]:
#                     minimum = [heights[start], start]
#                 start += 1
            
#             return minimum[1]
        
#         n = len(names)
#         curr = n - 1
        
#         while curr >= 0:
            
#             mn = search_minimum(0, curr)
            
#             heights[mn], heights[curr] = heights[curr], heights[mn]
#             names[mn], names[curr] = names[curr], names[mn]
            
#             curr -= 1
            
#         return names
                
            
# insertion sort

# Time: O(N^2)
# Space: O(1)

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      
        n = len(names)
        
        for index in range(1, n):
                # swap
                if heights[index] > heights[index - 1]:
                    for i in range(index, 0, - 1):
                        if heights[i] > heights[i - 1]:
                            heights[i], heights[i - 1] = heights[i - 1], heights[i]
                            names[i], names[i - 1] = names[i - 1], names[i]
        
        return names
                                                                            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

