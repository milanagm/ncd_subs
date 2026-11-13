class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_p = 0
        r_p = len(s) -1

        while l_p < r_p:
            if not l_p.allnum:
                l_p += 1
                continue
            if not r_p.allnum:
                r_p -= 1
                continue
            if l_p.small() != r_p.small():
                return False
        
        return True
        