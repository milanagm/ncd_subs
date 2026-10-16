class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        for i in nums: 
            p = target - i 
            if p in nums: 
                nums.index(p)
                return [nums.index(i), nums.index(p)]