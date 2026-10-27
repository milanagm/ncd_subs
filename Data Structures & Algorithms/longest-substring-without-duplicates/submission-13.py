class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        sub_len = 0

        for i, v in enumerate(s): 

            if i not in seen:
                seen.add(i)
                sub_len += 1
                max_len = max(max_len, sub_len)
            else: 
                # alles vor dem letzten vorkommen weg tun...wie ging das bloss
                max_len = max(max_len, sub_len)
            
        return max_len

           