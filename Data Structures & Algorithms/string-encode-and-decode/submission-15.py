class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            sub = ""
            sub += str(len(s))
            sub += "#"
            sub += s
            ret += sub
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            l = ""
            while i != "#":
                l += i
                i += 1 #ändert es i nur innerhalb der schleife?
            l = int(l)
            i += 1 # überspringen #

            word = ""
            for p in range(i, l):
                word += s[p]
                i += 1
            ret.append(word)
        return ret

            
        



        