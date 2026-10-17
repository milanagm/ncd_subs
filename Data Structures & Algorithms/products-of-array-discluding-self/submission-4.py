class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out  = [1] * len(nums)
        reli = [1] * len(nums)
        lire = [1] * len(nums)

        prev = 1
        for i in reli:
            reli[i] = prev
            prev *= reli[i]
        
        past = 1
        for i in range(len(lire) -1, -1, -1): 
            lire[i] = past
            past *= lire[i]
        
        for i in out:
            if i == 0:
                out[i] = lire[i]
            if i == len(out) - 1:
                out[i] = reli[i]
            out[i] = reli[i] * lire[i]

        return out
        