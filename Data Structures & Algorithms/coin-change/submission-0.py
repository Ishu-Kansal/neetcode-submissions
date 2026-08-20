class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        leftOver = amount
        coins = sorted(coins)
        numCoins = [0] * (amount+1)
        
        for i in range(1, amount + 1):
            minCoins = amount + 1
            for coin in coins:
                if(i >= coin and numCoins[i - coin] < minCoins and numCoins[i - coin] != -1):
                    minCoins = numCoins[i - coin]
            if(minCoins == amount + 1):
                numCoins[i] = -1
            else: 
                numCoins[i] = minCoins + 1
        
        print(numCoins)
        return numCoins[amount]

