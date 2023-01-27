class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        count = 0
        
        for index, value in enumerate(heights):
            if value != expected[index]:
                count += 1
        
        return count