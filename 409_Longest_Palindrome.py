class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = [0] * 52
        for c in s:
            if ord(c) >= ord('a'):
                counts[26 + ord(c) - ord('a')] += 1
            else:
                counts[ord(c) - ord('A')] += 1
        ret = 0
        oddLen = False
        for cnt in counts:
            if (not oddLen) and cnt & 1:
                oddLen = True
                ret += 1
            ret += cnt & 0b11111111110
        return ret