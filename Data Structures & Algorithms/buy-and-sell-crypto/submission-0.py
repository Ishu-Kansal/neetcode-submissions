class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]

        for i in range(len(prices)):
            if(prices[i] - min_buy > profit):
                profit = prices[i] - min_buy
            elif(prices[i] < min_buy):
                min_buy = prices[i]

        return profit