class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        p = 0
        m_l = 0
        s_l = 0
        for i in range(len(s)):
            if s[i] not in seen: 
                s_l += 1
                seen.add(s[i]) 
            else:
                while s[i] in seen:
                    seen.remove(s[p])
                    p += 1
            m_l = max(m_l, s_l)   
        return m_l
       