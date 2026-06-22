class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                lowIndex = i

            elif prices[i] - low > profit:
                profit = prices[i] - low
        return profit