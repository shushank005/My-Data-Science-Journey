# LeetCode Problem: 238. Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/

def Product_Of_Array_Except_Self(num):
    """
    Finds the product of all elements except the current one without using division.
    Approach: Prefix and Suffix Product arrays.
    Complexity: Time $O(N)$, Space $O(N)$
    """
    n = len(num)
    left_product = [1] * n
    right_product = [1] * n
    output = [0] * n

    # Step 1: Calculate Left Products
    for i in range(1, n):
        left_product[i] = left_product[i-1] * num[i-1]

    # Step 2: Calculate Right Products
    for i in range(n-2, -1, -1):
        right_product[i] = right_product[i+1] * num[i+1]

    # Step 3: Multiply Left and Right to get the final answer
    for i in range(n):
        output[i] = left_product[i] * right_product[i]
        
    return output

# --- 🧪 Hands-on Practice Examples ---
# print(f"Test 1 [9,0,-2]: {Product_Of_Array_Except_Self([9, 0, -2])}") # Output: [0, -18, 0]
# print(f"Test 2 [1,2,3,4]: {Product_Of_Array_Except_Self([1, 2, 3, 4])}") # Output: [24, 12, 8, 6]