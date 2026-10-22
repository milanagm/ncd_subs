class Solution:
    def isPalindrome(self, s: str) -> bool:
        p_l = 0
        p_r = len(s) - 1
        if len(s) > 0:
            while p_l < p_r: 
                if s[p_l] != s[p_r]:
                    return False
                p_l += 1
                p_r += 1
        
        return True
        