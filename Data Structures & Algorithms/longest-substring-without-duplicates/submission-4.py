class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = []
        for i in s: 
            if i not in sub: 
                sub.append(i)
            else: 
                max_len = max(max_len, len(sub))
                sub = [i]
        max_len = max(max_len, len(sub))
        return max_len

        