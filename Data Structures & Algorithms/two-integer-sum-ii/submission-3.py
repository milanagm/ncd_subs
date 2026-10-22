class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_l = 0
        p_r = len(numbers) -1 

        while p_l < p_r: 
            current_sum = numbers[p_l] + numbers[p_r]
            diff = target - current_sum
            if diff > 0: 
                # e.g. diff = 3 - 2
                p_l += 1 
                continue               
            if diff < 0: 
                p_r -= 1
                continue
            if diff == 0: 
                return [p_l + 1, p_r + 1]
        
