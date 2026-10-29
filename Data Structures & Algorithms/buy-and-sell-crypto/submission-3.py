class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_sum = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_sum = max(max_sum, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r = r + 1

        return max_sum
