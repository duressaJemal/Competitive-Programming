class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        store = [float("-inf")] * 3

        for num in nums:
            if num not in store:
                if num > store[0]:
                    store[0] = num
                    store.sort()
                
        if float("-inf") in store:
            return max(store)
        
        return store[0]
                
        
