class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_s = ""
        for s in strs:
            encode_s = encode_s + str(len(s)) + "#" + s

        return encode_s

    def decode(self, s: str) -> List[str]:
        decode_s = []
        i = 0
        while i< len(s):
            sub_s = s[i:]
            decode_l = sub_s.split('#')
            str_n = decode_l[0]
            decode_s.append(sub_s[len(str_n) + 1 : len(str_n) + 1 + int(str_n)])
            i += len(str_n) + int(str_n) + 1
        return decode_s