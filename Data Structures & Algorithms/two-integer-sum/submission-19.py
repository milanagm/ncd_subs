class Solution:
    def twoSum (self, nums:List[int], target: int) -> List[int]:
        for i, v in enumerate(nums): 
            complement = target - v
            if complement in nums:
                cmplmentIndx = nums.index(target - v)
                if i != cmplmentIndx:
                    return [i, cmplmentIndxa] 
