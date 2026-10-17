class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) 
            out += "#"
            out += s
        return out
      
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            l = ""
            #j = i
            while s[i] != "#":
                l += s[i]
                i +=1
            i +=1

            word = ""
            j = 0
            while j < int(l):
                word += s[i]
                j +=1
                i +=1
            out.append(word)
        return out
        