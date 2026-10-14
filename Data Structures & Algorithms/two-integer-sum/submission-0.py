class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        counter = {}

        for index, value in enumerate(nums): 
            if (target - value) in counter: 
                return [counter.get(target-value), index]
            else:
                counter[value] = index
            

         