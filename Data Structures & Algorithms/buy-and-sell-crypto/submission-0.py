class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        p_l = 0 
        p_r = len(prices) - 1

        while p_l < p_r: 
            profit = max(profit, prices[p_r] - prices[p_l])
            if prices[p_r] - prices[p_l] > 0: 
                prices[p_l] -=1
            if prices[p_r] - prices[p_l] < 0: 
                prices[p_r] +=1

        return profit
        
        