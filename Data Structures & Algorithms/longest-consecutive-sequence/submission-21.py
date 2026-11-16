class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = []
        length = 0
        for i in nums:
            if i-1 not in seen:
                sub_len = 1
                while i + sub_len in seen:
                    sub_len += 1
            length = max(length, sub_len)
        return length
