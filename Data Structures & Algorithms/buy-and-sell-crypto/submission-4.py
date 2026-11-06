class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0 
        for i in prices: 
            for j in range(i+1, len(prices)):
                if prices[j] - i > max_prof:
                    max_prof = prices[j] - i
        return max_prof

                              
                        

        