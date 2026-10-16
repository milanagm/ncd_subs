class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearance = []

        for i in nums:
            if i not in appearance: 
                appearance.add(i)
            else:
                return true
        return false