class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        min_try = 1
        max_try = max(piles)

        while min_try <= max_try: 
            k = min_try + (max_try - min_try)

            for i in piles: 
                needed_t = 0
                needed_t += piles[i] // k
            
            if needed_t <= h: 
                return k
            else: 
                min_try = k + 1 

        return k 
        