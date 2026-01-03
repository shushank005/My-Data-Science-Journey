# LeetCode Problem: 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/

def Maximum_Subarray_sum(num):
    """
    Finds the maximum sum of a contiguous subarray using Kadane's Algorithm.
    Complexity: Time $O(N)$, Space $O(1)$
    """
    curr = 0
    max_sum = float("-inf") 
    
    for i in range(len(num)):
        
        curr += num[i]
        
        
        max_sum = max(max_sum, curr)
        
        
        if curr < 0:
            curr = 0
            
    return max_sum

# --- 🧪 Hands-on Practice Examples ---

#print(f"Test 1: {Maximum_Subarray_sum([5,4,-1,7,8])}") # Output: 23
# print(f"Test 2: {Maximum_Subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])}") # Output: 6
# print(f"Test 3: {Maximum_Subarray_sum([-1, -2, -3])}") # Output: -1