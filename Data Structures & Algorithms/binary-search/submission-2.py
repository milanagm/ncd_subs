class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)< 2: 
            return 0

        i = int(len(nums)/ 2) #mitte
        
        while nums[i] >= target:
            if nums[i] == target: 
                return i
            if nums[i] > target: 
                i -= 1 

        while nums[i] >= target:
            if nums[i] == target: 
                return i
            if nums[i] < target: 
                i += 1
        
        return -1
        