class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)< 2: 
            return 0

        mitte = int(len(nums)/ 2)
        
        while nums[mitte] >= target:
            if nums[mitte] == target: 
                return i
            if nums[mitte] > target: 
                mitte -= 1 

        while nums[mitte] >= target:
            if nums[mitte] == target: 
                return i
            if nums[mitte] < target: 
                mitte += 1
        
        return -1
        