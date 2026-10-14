class Solution:
    def isAnagram (self, s: str, t: str) -> bool: 
    # idee: alphabetisch sortieren und vergleichen
        s = sorted(s)
        t = sorted(t)
        if s == t: 
            return True
        return False