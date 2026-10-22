class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_s = sorted(nums)
        answer = []
        # -2 -1 0 1 2
        for i, v in enumerate(nums_s): 
            p_l =  i + 1
            p_r = len(nums) - 1
            while p_l < p_r: 
                c_sum = nums_s[i] + nums_s[p_l] + nums_s[p_r]
                diff = 0 - c_sum
                if diff > 0:
                    p_l += 1
                    continue
                if diff < 0: 
                    p_r -= 1
                    continue
                if diff == 0:
                    if i != p_l and i != p_r and p_l!= p_r:
                        if sorted([nums_s[i], nums_s[p_l], nums_s[p_r]]) not in answer:
                            answer.append(sorted([nums_s[i], nums_s[p_l], nums_s[p_r]]))
                    p_l += 1
                    p_r -= 1
        return answer

       

