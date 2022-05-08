class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        prefix = [0] * (len(gain) + 1)
        
        for i in range(1, len(gain) + 1):
            prefix[i] = prefix[i - 1] + gain[i - 1]

        return max(prefix)
        
