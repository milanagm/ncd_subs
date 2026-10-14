class Solution:
    def hasDuplicate (self, nums:List[int]) -> bool: 
        counter = set()
        nums.sort()
        for i in nums: 
            if i in counter: 
                return True 
            else: 
                counter.add(i)
        return False