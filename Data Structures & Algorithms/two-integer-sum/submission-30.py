class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums): 
            p_v = target - v 
            if p_v in nums and i != nums.index(p_v):
                nums.index(p_v)
                return [i, nums.index(p_v)]
            