class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_store_s = {}

        for c in s:
            if c in char_store_s:
                char_store_s[c] += 1
            else:
                char_store_s[c] = 1
        
        for c in t:
            if  c not in char_store_s or char_store_s[c] == 0:
                return False
            char_store_s[c] -= 1
        total_count = 0
        for val in char_store_s.values():
            total_count += val
        
        if total_count != 0:
            return False
        
        return True