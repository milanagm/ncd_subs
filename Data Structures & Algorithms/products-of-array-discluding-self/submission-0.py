class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        pref = 1
        for i in nums:
            result.append(pref)
            pref *= i

        suf = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suf
            suf *= nums[i]
        
        return result

