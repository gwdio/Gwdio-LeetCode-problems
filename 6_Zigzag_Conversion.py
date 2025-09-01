import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        slen = len(s)
        if numRows == 1 or numRows >= slen:
            return s
        cpz = 2 * (numRows - 1)
        itrs = math.ceil(slen / cpz)
        out = list()
        for i in range(numRows):
            for j in range(itrs):
                if j*cpz + i < slen:
                    out.append(s[j*cpz + i])
                if (not (i == 0 or i == numRows - 1)) and (j+1)*cpz - i < slen:
                    out.append(s[(j+1)*cpz - i])
            
        return "".join(out)
