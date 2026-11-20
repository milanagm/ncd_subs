class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0 1 2 3
        l = [1]*len(nums)
        park = 1
        for i in range(len(nums)): 
            l[i] = park
            park *= nums[i]
        
        # 3 2 1 0
        r = [1] * len(nums)
        park = 1
        for i in range(len(nums)-1, -1, -1): # wie ging es mit reversed?
            r[i] = park
            park *= nums[i]

        result = l
        for i in range(len(result)): 
            result[i] *= r[i]
        
        return result




        