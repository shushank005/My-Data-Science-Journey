# LeetCode Problem: 167. Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Approach:
# My approach utilizes the two-pointer technique, which is efficient for sorted arrays.
# One pointer (`left`) is initialized at the beginning of the array, and the other (`right`) at the end.
# The algorithm iterates through the array, calculating the sum of the values at the two pointers.
# - If the sum equals the target, the solution is found.
# - If the sum is greater than the target, the `right` pointer is decremented to decrease the sum.
# - If the sum is less than the target, the `left` pointer is incremented to increase the sum.
# This process continues until the pointers meet, guaranteeing a solution with O(n) time complexity.

class Solution(object):
    def TwoSum(self,numbers: list[int], target: int) -> list[int]:
        """
        Finds two numbers in a sorted array that add up to a specific target.
        This function assumes the input array 'numbers' is sorted in non-decreasing order.
        """
        left = 0
        right = len(numbers) - 1
    
        while left < right:
            current_sum = numbers[left] + numbers[right]
        
            if current_sum == target:
                # LeetCode asks for 1-based indices, so we add 1.
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else: # current_sum < target
                left += 1

# Example Usage:
# result = TwoSum([2, 7, 11, 15], 9)
# print(result) # Expected output: [1, 2]