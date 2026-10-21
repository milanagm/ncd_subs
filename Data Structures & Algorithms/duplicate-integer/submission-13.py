class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = set()
        for i in nums: 
            if i in nums: 
                return True
            nums.add(i)
        return False
            
      