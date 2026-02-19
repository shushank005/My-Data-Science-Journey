# Problem: Find First and Last Position of Element in Sorted Array

# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Approach:
# Use Binary Search twice on the sorted array.
# First search moves left after finding target → gives first occurrence.
# Second search moves right after finding target → gives last occurrence.
# Return both indices; if target not found, return -1.

# Time Complexity: O(log n)

# Space Complexity: O(1)

# Code:
def Find_First_Last_Position(nums,target):
    def first_position(num,target):
        l,r = 0,len(num)-1
        ind = -1
        while l<=r:
            m = l + (r-l)//2
            if num[m] == target:
                ind = m
                r = m - 1
            elif num[m] < target:
                l = m + 1
            else:
                r = m - 1
        return ind
    def last_position(num,target):
        l,r = 0, len(num)-1
        ind = -1
        while l<=r:
            m = l + (r-l)//2
            if num[m] == target:
                ind = m
                l = m + 1
            elif num[m] < target:
                l = m + 1
            else:
                r = m - 1
        return ind
    return [first_position(nums,target),last_position(nums, target)]

# --- 🧪 Testing ---
# print(Find_First_Last_Position([5,7,7,8,8,10], 11))
