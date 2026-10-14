class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            match = target - value
            if match in seen:
                return [seen[match], i]
            seen[value] = i