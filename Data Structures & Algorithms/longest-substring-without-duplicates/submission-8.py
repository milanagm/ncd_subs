class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_max = 0
        len_sub = 1
        for e in s: #war for i in s iterieren über elements oder index? 
            p = e + 1
            while p == e: 
                len_sub += 1
                p += 1
                #continue #muss mans am ende der while schleife immer haben? 
            len_max = max(len_max, len_sub)
            

        return len_max
       