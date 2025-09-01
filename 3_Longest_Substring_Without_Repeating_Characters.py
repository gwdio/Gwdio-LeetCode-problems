class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        presence = [False]*95
        maxlen = 0
        clen = 0
        sidx = eidx = 0
        while eidx != len(s):
            while presence[self.getChar(s[eidx])]:
                presence[self.getChar(s[sidx])] = False
                sidx += 1
                clen -= 1 
            presence[self.getChar(s[eidx])] = True
            eidx += 1
            clen += 1
            maxlen = max(maxlen, clen)
        return maxlen


    def getChar(self, c: str):
        return ord(c) - 32
        