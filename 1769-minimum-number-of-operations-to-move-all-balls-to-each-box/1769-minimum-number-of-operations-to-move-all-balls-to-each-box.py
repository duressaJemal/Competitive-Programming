class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        output = []
        
        for index, value in enumerate(boxes):
            operations = 0
            for i in range(n):
                if boxes[i] == "1":
                    operations += abs(index - i)
            
            output.append(operations)
        
        return output
                
            
            
            
            
            
            
            
            
            
            
            
        
        