# Optimized

# Time: O(N)
# Space: O(1)

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        output = [0] * n
        
        left_count = 0
        right_count = 0
        
        left_sum = 0
        right_sum = 0
        
        # calculate number of 1's to the right and sum their index's
        for index in range(n):
            if boxes[index] == "1":
                right_count += 1
                right_sum += index

        for index in range(n):
            
            if boxes[index] == "1":
                left_count += 1
                right_count -= 1
                
                left_sum += index
                right_sum -= index

            left_value = abs(left_sum - (index * left_count))
            right_value = abs(right_sum - (index * right_count))
            
            output[index] = left_value + right_value
        
        return output
            


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
        
        # count all the values of "1"
        right_count = 0
        for index in range(n):
            if boxes[index] == "1":
                right_count += 1
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
            


        
        
        
        
        
        
        
                
        
        
        
        
        
            
            
            
            
            
            
        
        