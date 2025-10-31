class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 1
        counting = False
        for c in s[::-1]:
            if counting:
                if c != ' ':
                    count += 1
                else:
                    return count
            if c == ' ':
                continue
            else:
                counting = True
        return count