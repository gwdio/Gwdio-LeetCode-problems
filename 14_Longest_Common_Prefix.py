from typing import List


class Solution:
    def getChars(self, string: str, numchars: int) -> str:
        if len(string) < numchars:
            return ""
        return string[0:numchars]
    
    def shortestString(self, strs: List[str]) -> int:
        i = 200
        for s in strs:
            i = min(i, len(s))
        return i

    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = self.shortestString(strs)
        for i in range(1, shortest + 1):
            prefix = self.getChars(strs[0], i)
            for s in strs:
                pre = self.getChars(s, i)
                if pre != prefix:
                    return prefix[0:i-1]
        return strs[0][0:shortest]



