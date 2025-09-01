class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        key = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        for i in range(len(s)-1):
            if key[s[i]] < key[s[i+1]]:
                sum = sum - key[s[i]]
                continue
            sum += key[s[i]]
        sum += key[s[len(s)-1]]
        return sum
             
            