# LeetCode Problem: 724. Find Pivot Index
# Link: https://leetcode.com/problems/find-pivot-index/

def find_pivot_index(num):
    """
    Finds the index where the sum of numbers to the left equals the sum to the right.
    Approach: Prefix Sum / Running Sum
    Complexity: Time O(N), Space O(1)
    """
    left_sum = 0
    total_sum = sum(num) 
    
    for i in range(len(num)):

        right_sum = total_sum - left_sum - num[i]
        
        if right_sum == left_sum:
            return i
            
        left_sum += num[i]
        
    return -1

# --- 🧪 Testing ---
# print(f"Pivot Index: {find_pivot_index([1,7,3,6,5,6])}") # Output: 3