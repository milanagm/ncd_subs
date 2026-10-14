class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:

        for i, v in enumerate(nums):
            p = target - v
            if p in nums and nums.index(p) != i:
                    return sorted([i, nums.index(p)])
