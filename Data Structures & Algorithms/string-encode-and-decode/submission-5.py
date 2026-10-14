class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            l_s = len(s)
            encoded += str(l_s)
            encoded += "#"
            encoded += s
        return encoded
     
    def decode(self, s: str) -> List[str]:
        # "2#ab2#cd"
        decoded = []
        i = 0

        while i < len(s): 
            l_w = ""
            while s[i] != "#":
                l_w += s[i]
                i +=1
            l_w = int(l_w)
            i +=1

            word = ""
            for j in range(l_w):
                word += s[i]
                i += 1
                j += 1 
            decoded.append(word)

        return decoded
