class Solution:
    def longestPalindrome(self, s: str) -> str:
        # cacddleef
        longestLen = [-1, -1]
        longest = -1
        if(len(s) == 1 or len(s) == 0):
            return s
        for i in range(len(s)):
            left = i
            right = i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if(right - left > longest):
                    longest = right - left
                    longestLen = [left, right]
                left -= 1
                right += 1
            
            left = i-1
            right = i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if(right - left > longest):
                    longest = right - left
                    longestLen = [left, right]
                left -= 1
                right += 1
            

        
        return s[longestLen[0]:longestLen[1]+1]