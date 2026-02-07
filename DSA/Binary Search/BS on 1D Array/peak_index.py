# Problem: Peak Index in a Mountains Array (852)

# Link: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

# Approach: 
# Apply binary search on the array.
# Compare mid element with mid + 1.
# If arr[mid] < arr[mid + 1], move to the right half.
# Else, move to the left half the peak lies there.

# Time Complexity: O(log n)

# Space Complexity: O(1)

# Code:
def Peak_Index_Mountain(nums):
    low = 0
    high = len(nums)-1
    while low < high:

        mid = low + (high-low)//2
        if nums[mid] < nums[mid+1]:
            low = mid + 1

        else:
            high = mid
            
    return low

# --- 🧪 Testing ---
# print(Peak_Index_Mountain([0,1,3,6,4,2]))  Output: 3