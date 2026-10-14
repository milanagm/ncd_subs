class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            l = len(s)
            encoded += str(l)
            encoded += "#"
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            length_str = ""
            while s[i] != "#":
                length_str += s[i]
                i += 1

            length = int(length_str)
            i += 1  # das "#" überspringen

            word = ""
            count = 0
            while count < length:
                word += s[i]
                i += 1
                count += 1

            decoded.append(word)
        return decoded
