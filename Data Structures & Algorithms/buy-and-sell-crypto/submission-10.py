class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in prices:
            for j in range(i+1, len(prices)):
                prof = max(prof, prices[j]-i)
        return prof