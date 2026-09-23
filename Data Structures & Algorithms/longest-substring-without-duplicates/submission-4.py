class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contained = set()
        i = 0
        j = 0
        longestLen = 0
        while(i < len(s)):
            if(s[i] in contained):
                while(s[i] in contained):
                    contained.remove(s[j])
                    j += 1
            contained.add(s[i])
            i += 1
            longestLen = max(longestLen, i - j)
        return longestLen
