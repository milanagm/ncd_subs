class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final_h = 0 
        final_l = 0
        current_max = 0 

        for i in range(len(heights)):
            p_l = len(heights) - 1

            while i < p_l: 
                h = min(heights[i], heights[p_l])
                l = p_l - i
                product = h * l
                if product > current_max: 
                    current_max = product
                    final_h = h
                    final_l = l
                p_l -= 1

        return final_h * final_l
        
        
        