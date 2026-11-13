class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        
        for i in range(prices):
            p_l = i + 1
            for p_l in range(len(prices)): 
                profit = max(prices[p_l]-prices[i], profit)

        return profit