# LeetCode Problem: 560. Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

def Subarray_Sum_Equals_K(num, k):
    """
    Finds the total number of continuous subarrays whose sum equals to k.
    Approach: Prefix Sum + Hashmap (Frequency Tracking)
    Complexity: Time O(N), Space O(N)
    """
    hashmap = {0: 1}
    count = 0
    current_sum = 0
    
    for i in range(len(num)):
        
        current_sum += num[i]
        
        old_sum = current_sum - k
        if old_sum in hashmap:
            
            count += hashmap[old_sum]
        
        hashmap[current_sum] = hashmap.get(current_sum, 0) + 1
        
    return count

# --- 🧪 Hands-on Practice Examples ---
# print(f"Subarrays Count: {Subarray_Sum_Equals_K([1, -1, 1, 1, 1, 1], 3)}") # Output: 4