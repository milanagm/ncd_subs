class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inside = set(nums)
        seen = set()
        max_length= 0

        for i in nums: 
            length = 1
            if i not in seen:
                seen.add(i)
                while i+length in inside: 
                    seen.add(i+length)
                    length += 1
                max_length = max(max_length, length)
       
        return max_length