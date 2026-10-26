class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #bacaa mit k = 1
        max_len = 0
        i = 0
        k_sub = k

        while i < len(s) - 1:
            sub_len = 0 
            j = i
            while j < len(s) - 1:
                if s[j+1] == s[j]:
                    sub_len += 1
                    j += 1
                    continue
                if s[j+1] != s[j]:
                    if k_sub > 0: 
                        k_sub -= 1
                        sub_len += 1
                        j += 1
                        continue
                    if k_sub == 0: 
                        max_len = max(max_len, sub_len)
                        k_sub = k
                        i += 1
                        continue
        return max_len






