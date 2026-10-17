class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out  = []
        reli = [] # wie macht man ein array einer best laenge?
        lire = []

        prev = 1
        for i in reli: #wie iteriere ich eine schleife von hinten
            reli[i] = prev
            prev *= reli[i]
        
        past = 1
        for i in lire: 
            lire[i] = past
            past *= lire[i]
        
        for i in out:
            if i == 0:
                out[i] = lire[i]
            if i == len(out) - 1:
                out[i] = reli[i]
            out[i] = reli[i] * lire[i]

        return out
        