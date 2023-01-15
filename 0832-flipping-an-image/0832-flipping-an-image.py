class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)
        
        for index in range(n):
            image[index].reverse()
            
            for i in range(n):
                image[index][i] = 1 - image[index][i]
        
        return image