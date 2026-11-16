class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        longest = 0
        sub_len = 0 
        for i in s:
            while i in seen:
                del seen[0]
                sub_len -= 1
            seen.append(i)
            sub_len += 1
            longest = max(longest, sub_len)

        return longest
        
       