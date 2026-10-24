class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        current_max = 0 
        
        while l < r: 
            h = min(heights[l], heights[r])
            w = r - l
            current_max = max(current_max, h * w)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return current_max

        
        