class NumArray:

    def __init__(self, nums: List[int]):
        
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        self.nums = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
