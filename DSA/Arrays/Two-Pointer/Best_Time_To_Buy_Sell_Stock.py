# LeetCode Problem: 121. Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def best_time_to_buy_sell_stock(prices):
    """
    Finds maximum profit by buying low and selling high Stock.
    Approach: Two-Pointer
    Complexity: Time O(N), Space O(1)
    """
    if len(prices) <= 1:
        return 0
    
    left = 0 
    profit = 0
    
    for right in range(1, len(prices)):
        
        if prices[right] > prices[left]:
            current_profit = prices[right] - prices[left]
            profit = max(profit, current_profit)
        
        else:
            left = right
            
    return profit

# --- 🧪 Testing ---
# print(f"Max Profit: {best_time_to_buy_sell_stock([7,1,5,3,6,4])}") # Output: 5