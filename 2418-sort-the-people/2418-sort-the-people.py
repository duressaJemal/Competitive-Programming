

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        n = len(names)
        
        name_height_map = {}
        for index, value in enumerate(names):
            name_height_map[heights[index]] = value
        
        # sort using bubble sort
        for iteration in range(n):
            for index in range(1, n):
                if heights[index] > heights[index - 1]:
                    heights[index], heights[index - 1] = heights[index - 1], heights[index]
                
        output = []
        for height in heights:
            output.append(name_height_map[height])
        
        return output