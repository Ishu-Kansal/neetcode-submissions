class Solution:
    def countBits(self, n: int) -> List[int]:
        if(n == 0):
            return [0]
        dp = [0, 1]
        lastPower = 1

        for i in range(2, n+1):
            if(i == lastPower * 2):
                dp.append(1)
                lastPower *= 2
            else:
                remainder = i - lastPower
                dp.append(1 + dp[remainder])
            
        
        return dp
