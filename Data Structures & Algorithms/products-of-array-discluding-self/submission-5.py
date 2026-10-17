class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out  = [1] * len(nums)
        reli = [1] * len(nums)
        lire = [1] * len(nums)

        prev = 1
        for i in range(len(reli)):
            reli[i] = prev
            prev *= nums[i]
        
        past = 1
        for i in range(len(lire) -1, -1, -1): 
            lire[i] = past
            past *= nums[i]
        
        for i in range(len(out)):
            if i == 0:
                out[i] = lire[i]
            if i == len(out) - 1:
                out[i] = reli[i]
            out[i] = reli[i] * lire[i]

        return out
        