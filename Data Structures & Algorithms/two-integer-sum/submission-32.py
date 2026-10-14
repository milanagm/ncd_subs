class Solution:
    def twoSum (self, nums: List[int], target: int) -> List[int]:
        indexer = {}

        for i, v in enumerate(nums): 
            p = target - v 
            if p in indexer: 
                return [indexer[p], i]
            else: 
                indexer[v] = i

