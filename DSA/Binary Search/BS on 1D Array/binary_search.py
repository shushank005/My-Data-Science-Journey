# Problem: Binary Search (704)

# Link: https://leetcode.com/problems/binary-search/description/

# Approach:
# The array is sorted, so I use binary search.
# I keep left and right pointers and check the middle element.
# Based on comparison with target, I move to left or right half.
# If I find the target, I return its index, otherwise return -1.

# Time Complexity: O(log n)

# Space Complexity: O(1)

# Code:
def Binary_search(num,target):
    left = 0
    right = len(num)-1
    while left <= right:
        mid = left + (right-left) //2

        if num[mid] == target:
            return mid
        
        elif num[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1

# --- 🧪 Testing ---
# print(Binary_search([2,3,4,5,7,9],7))  # output: 4