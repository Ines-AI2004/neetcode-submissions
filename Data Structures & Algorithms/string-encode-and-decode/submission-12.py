from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
           
            s_escape = s.replace("\\", "\\\\").replace(",", "\\,")
      
            res += s_escape + ","
        return res

    def decode(self, s: str) -> List[str]:
        r = []
        cur = ""
        i = 0
        while i < len(s):
            if s[i] == "\\":
              
                cur += s[i + 1]
                i += 2
            elif s[i] == ",":
               
                r.append(cur)
                cur = ""
                i += 1
            else:
                cur += s[i]
                i += 1
        return r