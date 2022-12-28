# Link: https://leetcode.com/problems/convert-the-temperature/
#Q: 2469. Convert the Temperature

# Time: O(1)
# Space: O(1)

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        output = [0, 0]
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        output[0] = kelvin
        output[1] = fahrenheit
        
        return output
