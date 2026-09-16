from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if  len(s) != len(t):
            return False

        letter_map_s = Counter(s)
        letter_map_t = Counter(t)

        if letter_map_s == letter_map_t:
            return True
        return False

        
