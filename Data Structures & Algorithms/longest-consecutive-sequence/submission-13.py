class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        max_len = 0
        for i in range(len(nums)):
            if i not in seen: 
                length = 1
            while i+length in seen:
                length += 1

        return max_len
        