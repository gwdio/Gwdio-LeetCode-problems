class Solution:
    def processStr(self, s: str) -> str:
        sarr = []
        for c in s:
            match c:
                case '#':
                    sarr += sarr.copy()
                case '%':
                    sarr.reverse()
                case '*':
                    if sarr:
                        sarr.pop()
                case _:
                    sarr.append(c)
            # print(f"processed {c}: after: {"".join(sarr)}")
        return "".join(sarr)
                