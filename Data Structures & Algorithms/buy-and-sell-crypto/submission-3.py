class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        p_l = 0 
        p_r = 1
        while p_r < len(prices):                 
            profit = max(profit, prices[p_r] - prices[p_l])
            if prices[p_r] < prices[p_l]:       
                p_l = p_r
            p_r += 1   

        return profit

                              
                        

        