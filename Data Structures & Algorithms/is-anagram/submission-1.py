class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for ch in s:
            counts[ch] = 1 + counts.get(ch, 0)
        
        for c in t:
            if(c not in counts):
                return False
            counts[c] -= 1
        

        for letter in counts.keys():
            if(counts[letter] != 0):
                return False
        
        return True