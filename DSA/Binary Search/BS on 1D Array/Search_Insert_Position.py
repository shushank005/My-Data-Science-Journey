# Problem: Search Insert Position (35)

# Link: https://leetcode.com/problems/search-insert-position/description/

# Approach:
# We use Binary Search on a sorted array.
# If target is found, return its index.
# If not found, when loop ends, 'left' gives the correct insert position.

# Time Complexity: O(log n)

# Space Complexity: O(1)

# Code:
def Search_Insert_Position(num,target):
    left = 0
    right = len(num)-1
    while left <= right:
        mid = left + (right-left)//2

        if num[mid] == target:
            return mid
        
        elif num[mid]< target:
            left = mid + 1

        else:
            right = mid -1

    return left

# --- 🧪 Testing ---
# print(Search_Insert_Position([1,2,5,7,9],8))  Output: 4