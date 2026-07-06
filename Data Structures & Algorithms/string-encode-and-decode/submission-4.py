class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_s = ""
        for s in strs:
            enc_s += str(len(s)) + "#" + s
        
        return enc_s

    def decode(self, s: str) -> List[str]:
        dec_l = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            dec_l.append(s[j+1: j+1+length])
        
            i = j + 1 + length

        return  dec_l
