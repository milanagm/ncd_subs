class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inside = []
        for i, v in enumerate(nums): 
            diff = target - v
            if diff in nums and i != nums.index(diff):
                return sorted([i, nums.index(diff) ])
        