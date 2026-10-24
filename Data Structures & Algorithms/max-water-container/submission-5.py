class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final_h = 0 
        final_l = 0
        current_max = 0 
        
        while i < p_l: 
            h = min(heights[i], heights[p_l])
            l = p_l - i
            current_max = max(current_max, h * l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return current_max

        
        