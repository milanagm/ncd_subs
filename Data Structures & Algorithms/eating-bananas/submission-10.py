class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        min_try = 1
        max_try = max(piles)
        legit_k = max_try 

        while min_try <= max_try: 
            k = min_try + (max_try - min_try) // 2
            needed_t = 0

            for i in piles: 
                needed_t += (i + (k-1)) // k
            
            if needed_t <= h: 
                legit_k = k
                max_try = k - 1 
            else: 
                min_try = k + 1 

        return legit_k
        