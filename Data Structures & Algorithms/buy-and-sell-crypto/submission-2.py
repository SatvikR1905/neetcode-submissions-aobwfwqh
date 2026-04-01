class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[right] < prices[left]:
                left = right
            else:
                right += 1
        return max_profit

