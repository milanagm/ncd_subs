class Solution:
    def hasDuplicate (self, nums: List[int]) -> bool:
        contains = [] 
        for i in nums:
            if i in contains: 
                return True
            else: 
                contains.append(i)
        return False
        