class Solution:
    
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp[len(s)] = 1
        def recurse(i):
            if(i in dp):
                return dp[i]
            if(i == len(s)):
                return 1

            if(s[i] == '0'):
                dp[i] = 0
                return 0

            totalWays = recurse(i+1)

            if(i < len(s) - 1):
                twoDigit = int(s[i:i+2])
                if(twoDigit > 0 and twoDigit < 27):
                    totalWays += recurse(i+2)
            dp[i] = totalWays
            return totalWays
        return recurse(0)