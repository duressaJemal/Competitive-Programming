class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def reverse_num(num):
            generated = 0
            while num >= 1:
                generated = generated * 10 + num % 10
                num = num // 10
            return generated
        
        unique = set(nums)
        for num in nums:
            reversed_num = reverse_num(num)
            unique.add(reversed_num)
        
        return len(unique)