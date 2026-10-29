class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        for i in range(len(prices) - 1):
            max_return = max(prices[i + 1:]) - prices[i]
            if max_return > max_sum:
                max_sum = max_return
        return max(0, max_sum)