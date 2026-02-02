# LeetCode Problem: 49. Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/

def group_anagram(strs):
    """
    Groups words that are anagrams of each other using a Hashmap.
    Key: Sorted string, Value: List of original strings.
    """
    hashmap = {}
    
    for s in strs:
        
        sort_str = "".join(sorted(s))
        
        if sort_str not in hashmap:
            hashmap[sort_str] = []
        hashmap[sort_str].append(s)
        
    return list(hashmap.values())
