# LeetCode Problem: 152. Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/

def Maximum_Product_Subarray(num):
    """
    Finds the largest product of a contiguous subarray using Prefix & Suffix approach.
    Complexity: Time $O(N)$, Space $O(1)$
    """
    prefix = 1
    suffix = 1
    ans = float("-inf")
    
    n = len(num)
    for i in range(n):
        
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1
        
        
        prefix *= num[i]
        suffix *= num[n - 1 - i]
        
        ans = max(ans, prefix, suffix)
        
    return ans

# --- 🧪 Testing ---
# print(f"Product Result: {Maximum_Product_Subarray([2,3,-2,4])}")   -> Output: 6