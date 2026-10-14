class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:

        for i, v in enumerate(nums):
            diff = target - v
            if diff in nums: 
                diff_i = nums.index(diff)
                if diff_i != i:
                    return sorted([i, diff_i])