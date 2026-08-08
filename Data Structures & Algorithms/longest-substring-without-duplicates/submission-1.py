class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = set()
        longest = 0
        while(i < len(s)):
            currChar = s[i]
            if(currChar in seen):
                while(currChar in seen):
                    seen.remove(s[j])
                    j += 1
            seen.add(currChar)
            i += 1
            if(i - j > longest):
                longest = i - j

        return longest
