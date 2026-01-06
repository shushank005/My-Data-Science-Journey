# LeetCode Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/

def TwoSum(num, target):
    """
    Finds indices of two numbers that add up to the target.
    Approach: Hashing 
    Complexity: Time O(N), Space O(N)
    """
    hashmap = {} 
    
    for i, n in enumerate(num):
        diff = target - n
        
        if diff in hashmap:
            return [hashmap[diff], i]
        
        hashmap[n] = i
        
    return []

# --- 🧪 Testing ---
# print(f"Indices: {TwoSum([2, 11, 7, 15], 9)}") # Output: [0, 2]