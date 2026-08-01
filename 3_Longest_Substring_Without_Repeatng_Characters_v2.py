class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        hd, tl = 0, 0
        ln, maxln = 0, 0
        while hd < len(s):
            if not counts.setdefault(s[hd], 0):
                counts[s[hd]] += 1
                hd += 1
                ln += 1
                maxln = max(ln, maxln)
            else:
                while counts[s[hd]]:
                    counts[s[tl]] -= 1
                    tl += 1
                    ln -= 1
        return maxln

        