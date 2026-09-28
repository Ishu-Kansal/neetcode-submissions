class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueChars = set()

        for ch in s:
            uniqueChars.add(ch)
        
        uniqueChars = list(uniqueChars)
        
        longestLen = 0
        for ch in uniqueChars:
            i = 0
            j = 0
            numLeft = k
            while(i < len(s)):
                if(s[i] != ch):
                    if(numLeft > 0):
                        numLeft -= 1
                        i += 1
                    else:
                        while(s[j] == ch):
                            j += 1
                        j += 1
                        numLeft += 1
                else:
                    i += 1
                longestLen = max(longestLen, i - j)
        
        return longestLen