class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inside = set(nums)
        seen = set()
        max_length= 0
        sub_length = 0

        for i in nums: 
            length = 0
            if i not in seen:
                length += 1
                while i+length in inside: 
                    seen.add(i+1)
                    length += 1
                    max_length = max(max_length, sub_length)
       
        return max_length