from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # نضع \ قبل أي \ أو , داخل النص الأصلي
            s_escape = s.replace("\\", "\\\\").replace(",", "\\,")
            # ثم نضيف فاصلة التشفير في النهاية
            res += s_escape + ","
        return res

    def decode(self, s: str) -> List[str]:
        r = []
        cur = ""
        i = 0
        while i < len(s):
            if s[i] == "\\":
                # إذا وجدنا \ نأخذ الحرف الذي بعده مباشرة دون اعتباره فاصلة تشفير
                cur += s[i + 1]
                i += 2
            elif s[i] == ",":
                # فاصلة عادية مجردة تعني نهاية الكلمة الحالية
                r.append(cur)
                cur = ""
                i += 1
            else:
                cur += s[i]
                i += 1
        return r