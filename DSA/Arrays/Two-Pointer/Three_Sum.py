# LeetCode Problem: 15. 3Sum
# Link: https://leetcode.com/problems/3sum/

def three_sum(num):
    """
    Finds all unique triplets in the array which gives the sum of zero.
    Approach: Sorting + Two-Pointer
    """
    num.sort() 
    result = []
    
    for i in range(len(num)):
        
        if i > 0 and num[i] == num[i-1]:
            continue
            
        left = i + 1
        right = len(num) - 1
        
        while left < right:
            current_sum = num[i] + num[left] + num[right]
            
            if current_sum == 0:
                result.append([num[i], num[left], num[right]])
                
                while left < right and num[left] == num[left + 1]: left += 1
                while left < right and num[right] == num[right - 1]: right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

# --- 🧪 Testing ---
# print(f"3Sum Result: {three_sum([-1,0,1,2,-1,-4])}") # Output: [[-1, -1, 2], [-1, 0, 1]]