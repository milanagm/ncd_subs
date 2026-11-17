class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        m_l = 0
        for i in range(s):
            if s[i] not in seen:
                s_l = 1
                while  s[i] + s_l in seen:
                    s_l += 1
            m_l = max(m_l, s_l)
            seen.add(s[i])

        return m_l
       