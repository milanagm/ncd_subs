class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()                 # was []
        longest = 0
        sub_len = 0
        l = 0                        # new: left edge of window
        for i in s:
            while i in seen:         # O(1) lookup now
                seen.remove(s[l])    # was: del seen[0]
                l += 1
                sub_len -= 1
            seen.add(i)              # was: seen.append(i)
            sub_len += 1
            longest = max(longest, sub_len)

        return longest
        
       