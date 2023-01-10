# # Time: O(N^2)
# # Space: O(N)

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
        
#         n = len(boxes)
#         output = []
        
#         for index, value in enumerate(boxes):
#             operations = 0
#             for i in range(n):
#                 if boxes[i] == "1":
#                     operations += abs(index - i)
            
#             output.append(operations)
        
#         return output

    
# Time: O(N)
# Space: O(N)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        prefix = [0] * n
        output = [0] * n
        
        # build prefix sum for index's with value of "1"
        for index in range(1, n):
            prefix[index] = prefix[index - 1]
            if boxes[index] == "1":
                prefix[index] += index
                
        right_count = sum(list(map(int, list(boxes))))
        left_count  = 0
        
        for index in range(n):
            
            if boxes[index] == "1":
                right_count -=1
                left_count += 1
                
            left_sum = prefix[index]
            right_sum = prefix[-1] - prefix[index]
            
            left_value = abs(left_sum - (index * left_count))
            right_value = abs(right_sum - (index * right_count))
            
            output[index] = left_value + right_value

        
        return output
            
            
            
            
            
            
            
            
            
            
        
        