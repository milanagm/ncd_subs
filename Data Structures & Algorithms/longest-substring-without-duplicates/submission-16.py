class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        sub_len = 0
        remove_pointer = 0

        for i, v in enumerate(s): 

            if v not in seen:
                seen.add(i)
                sub_len += 1
                max_len = max(max_len, sub_len)
            else: 
                while v in seen: 
                    seen.remove([remove_pointer])
                    remove_pointer += 1

                max_len = max(max_len, sub_len)
            
        return max_len

           