class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s))
            encode += "#"
            encode += s
        return encode
   

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1
            i +=1
            length = int(length)

            word = ""
            j = 0
            while j < length: 
                word += s[i]
                i += 1
                j += 1
            decoded.append(word)

        return decoded
