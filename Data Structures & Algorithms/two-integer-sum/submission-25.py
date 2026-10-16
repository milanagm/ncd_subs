class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:

        for i, v in enumerate(nums):
            p = target - v
            if p in nums:
                if nums.index(p) != i:
                    return [i, nums.index(p)] 
