class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        seen = {}
        longest = 0
        while(i < len(s)):
            currChar = s[i]
            if(currChar in seen):
                while(currChar in seen):
                    seen[s[j]] -= 1
                    if(seen[s[j]] <= 0):
                        seen.pop(s[j])
                    j += 1
            seen[currChar] = 1 + seen.get(currChar, 0)
            i += 1
            if(i - j > longest):
                longest = i - j

        return longest
