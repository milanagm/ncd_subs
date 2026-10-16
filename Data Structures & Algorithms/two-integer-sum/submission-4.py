class Solution:
    def twoSum(self, nums:  int, target: int) -> List[int]:
        for i, value in enumerate(nums): 
            match = target - value
            if match in nums and match != value: 
                return [i, nums.index(match)]