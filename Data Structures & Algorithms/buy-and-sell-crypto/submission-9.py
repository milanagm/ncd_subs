class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices)):
            for p_l in range(i+ 1, len(prices)): 
                profit = max(prices[p_l]-prices[i], profit)

        return profit