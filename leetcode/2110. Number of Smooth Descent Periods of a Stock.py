#link 

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        # OPTIMIZED
        
        total = 0
        number_size = 1
        
        for i in range(1, len(prices)):

            if prices[i - 1] - prices[i] == 1:
                number_size += 1
            else:
                total = total + (number_size * (number_size + 1))//2
                number_size = 1
            
        total = total + (number_size * (number_size + 1))//2
        return total
        
        # FIRST LOOK
        
#         store = []
#         start, end = 0, 1
        
#         while end < len(prices):
            
#             if prices[end - 1] - prices[end] == 1:
#                 end += 1
#             else:
#                 store.append(prices[start : end])
#                 start = end
#                 end += 1
         
#         store.append(prices[start : end])
        
#         output = 0
#         for num in store:
            
#             if len(num) == 1:
#                 output += 1
#             else:
#                 output += (len(num) * (len(num) + 1))//2
            
#         return output
                
                
                
