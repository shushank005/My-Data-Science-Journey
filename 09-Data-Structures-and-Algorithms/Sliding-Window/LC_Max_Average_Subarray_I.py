# LeetCode Problem: 643. Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/

# Approach:
# My approach utilizes the sliding window technique for an efficient O(n) solution.
# I initialize a window of size k and calculate its initial sum, while also tracking
# the maximum sum found. Then, I iterate through the rest of the array, sliding the
# window one element at a time by adding the new element and subtracting the element
# that is leaving the window. After each slide, I update max_sum if the new
# window's sum is larger. Finally, the function returns max_sum divided by k.

def maxAverageSubArray(nums: list[int], k: int) -> float:
    """
    Finds the maximum average of all contiguous subarrays of size k.
    """
    left = 0
    window_sum = 0
    max_sum = float('-inf')

    for right in range(len(nums)):
        # Add the current element to the window sum
        window_sum += nums[right]

        # Once the window is of size k, start calculating and sliding
        if (right - left + 1) == k:
            # Update the maximum sum found so far
            max_sum = max(max_sum, window_sum)
            
            # Slide the window: subtract the leftmost element and move the left pointer
            window_sum -= nums[left]
            left += 1
            
    # Return the final maximum average
    return max_sum / k

# Example Usage:
# result = maxAverageSubArray([1, 12, -5, -6, 50, 3], 4)
# print(result) # Expected output: 12.75