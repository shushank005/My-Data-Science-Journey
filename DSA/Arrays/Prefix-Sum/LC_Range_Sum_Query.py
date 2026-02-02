# LeetCode Problem: 303. Range Sum Query - Immutable
# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Approach (Using your logic):
# My approach uses the Prefix Sum technique.
# In the constructor (__init__), I create a 'prefix_sum' array where
# prefix_sum[i] stores the sum of all numbers from nums[0] to nums[i].
#
# Then, when sumRange(left, right) is called:
# 1. If left is 0, the answer is just the total sum up to 'right', which is prefix_sum[right].
# 2. If left is greater than 0, the answer is the total sum up to 'right'
#    minus the total sum up to 'left - 1'. (prefix_sum[right] - prefix_sum[left - 1])

class NumArray:

    def __init__(self, nums: list[int]):

        self.prefix_sum = [0] * len(nums)
        self.prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]
            
    def sumRange(self, left: int, right: int) -> int:

        if left == 0:

            return self.prefix_sum[right]
        else:

            return self.prefix_sum[right] - self.prefix_sum[left - 1]


# --- Example Usage ---
# nums = [-2, 0, 3, -5, 2, -1]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2)) # Output: 1
# print(obj.sumRange(2, 5)) # Output: -1
# print(obj.sumRange(0, 5)) # Output: -3