class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums_s = sorted(nums)

        for i, v in enumerate(nums_s): 
            p_l = i + 1
            p_r = len(nums_s) - 1
            while p_l < p_r: 
                sum = v + nums_s[p_l] + nums_s[p_r]
                if sum == 0: 
                    if p_l != p_r and p_l != i and p_r != i: 
                        if [v, nums_s[p_l], nums_s[p_r]] not in answer: 
                            answer.append([v, nums_s[p_l], nums_s[p_r]])
                        p_l += 1
                        p_r -= 1
                        continue
                if sum < 0: 
                    p_l += 1
                    continue
                if sum > 0: 
                    p_r -= 1
                    continue
        
        return answer
       