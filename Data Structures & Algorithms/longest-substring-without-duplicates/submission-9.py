class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_max = 0
        len_sub = 1 # wird bei for i dann zurückgesetzt bei i + 1 ?

        for i, v in enumerate(s): 
            p = i + 1
            while s[p] == v: 
                len_sub += 1
                p += 1
                #continue #muss mans am ende der while schleife immer haben? 
            len_max = max(len_max, len_sub)
            

        return len_max
       