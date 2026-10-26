class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #bacaa mit k = 1
        max_len = 0

        while i < len(s):
            sub_len = 0 
            j = i
            while k > -1:
                while s[j+1] == s[j]:
                    sub_len += 1
                    j += 1
                if s[j+1] != s[j]:
                    if k > 0: 
                        k -= 1
                        




