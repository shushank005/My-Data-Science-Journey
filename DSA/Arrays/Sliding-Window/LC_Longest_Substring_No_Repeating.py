# LeetCode Problem: 3. Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Approach:
# My approach uses the sliding window technique with two pointers (left and right)
# and a set (unique) to keep track of characters currently in the window.

# 1. I iterate with the 'right' pointer, adding s[right] to the set.
# 2. If s[right] is already in the set, it means we have a repeating character.
# 3. I then move the 'left' pointer forward, removing s[left] from the set,
#    until the repeating character is gone from the window.
# 4. After each step, I add the new s[right] to the set and update the 'max_len'
#    by comparing it with the current window size (right - left + 1).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            
            unique_chars.add(s[right])
            
            max_len = max(max_len, right - left + 1)
            
        return max_len

# --- Example Usage ---
# sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb")) # Output: 3
# print(sol.lengthOfLongestSubstring("bbbbb"))    # Output: 1
# print(sol.lengthOfLongestSubstring("pwwkew"))   # Output: 3