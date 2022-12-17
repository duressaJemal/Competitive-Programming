# Link: https://leetcode.com/problems/range-sum-query-immutable/
#Q: 303. Range Sum Query - Immutable

class NumArray:

    # Time: O(N)
    # space: O(1)
    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.nums = nums

    # Time: O(1)
    # Space: O(1)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left - 1] if left > 0 else self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
