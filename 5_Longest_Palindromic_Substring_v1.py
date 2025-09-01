class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        n = len(s)

        i = 0
        while i < n:
            if i % 1 == 0:
                left = right = int(i)
            else:
                left = int(i - 0.5)
                right = int(i + 0.5)

            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            if right - left - 1 > len(longest):
                longest = s[left + 1:right]

            i += 0.5

        return longest

            
        