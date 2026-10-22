class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_s = sorted(nums)
        answer = []
        # -2 -1 0 1 2
        for i in nums_s: 
            p_l = 0 
            p_r = len(nums) - 1
            c_sum = nums_s[i] + nums_s[p_l] + nums_s[p_r]
            diff = 0 - c_sum
            if diff > 0:
                p_l += 1
                continue
            if diff < 0: 
                p_r -= 1
                continue
            if diff == 0 and i != p_l and i != p_r and p_l!= p_r:
                answer.append([i, p_l, p_r])
            
        return answer.set()

       

