class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            l = len(s)
            out += str(l)
            out += "#"
            out += s
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0 
        while i < len(s):
            l = ""
            j = i
            while s[j] != "#":
                l += str(s[j])
                j += 1
                i += 1
            i += 1

            word = ""
            c = 0 
            while c < int(l) - 1:
                word += s[i]
                i += 1
                c += 1
            
            out.append(word)

        return out

