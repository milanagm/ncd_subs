class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += s
            encoded += "#"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        sub_string = []

        for letter in s:
            if letter != "#":
                sub_string.append(letter)
            else:
                decoded.append("".join(sub_string))
                sub_string = []

        return decoded
