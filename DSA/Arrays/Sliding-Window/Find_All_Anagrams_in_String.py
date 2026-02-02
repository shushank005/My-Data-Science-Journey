# LeetCode Problem: 438. Find All Anagrams in a String
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

def Find_All_Anagrams_in_String(s, p):
    """
    Finds all start indices of p's anagrams in s.
    Approach: Sliding Window with Frequency Counters
    Complexity: Time O(N), Space O(1)
    """
    from collections import Counter
    
    if len(p) > len(s): return []
    
    result = []
    window_p = Counter(p) 
    window_s = Counter(s[:len(p)]) 
    
    if window_p == window_s:
        result.append(0)
        
    left = 0
    right = len(p)
    
    
    while right < len(s):
        
        new_ele = s[right]
        window_s[new_ele] += 1
        
        old_ele = s[left]
        window_s[old_ele] -= 1
        
        if window_s[old_ele] == 0:
            del window_s[old_ele]
            
        left += 1
        
        if window_s == window_p:
            result.append(left)
            
        right += 1
        
    return result

# --- 🧪 Testing ---
# print(f"Anagram Indices: {Find_All_Anagrams_in_String('cbaebabacd', 'abc')}") # Output: [0, 6]