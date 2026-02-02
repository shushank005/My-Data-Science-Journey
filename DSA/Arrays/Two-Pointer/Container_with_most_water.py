# LeetCode Problem: 11. Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

def Container_With_Most_Water(height):
    """
    Finds the maximum water a container can store.
    Approach: Two-Pointer Technique
    Complexity: Time O(N), Space O(1)
    """
    max_area = 0
    i = 0
    j = len(height) - 1
    
    while i < j:

        current_width = j - i
        current_height = min(height[i], height[j])
        area = current_width * current_height
        
        max_area = max(max_area, area)
        
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
            
    return max_area

# --- 🧪 Testing ---
# print(f"Max Water Area: {Container_With_Most_Water([1,8,6,2,5,4,8,3,7])}") # Output: 49