from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        goal = Counter(words)
        wordLen = len(words[0])
        window = len(words)
        res = []
        for offset in range(wordLen):
            curr = Counter()
            buff = 0
            for hd in range(offset, len(s), wordLen):
                # print(curr)
                word = s[hd:hd + wordLen]
                if word not in goal:
                    curr = Counter()
                    buff = 0
                    continue
                
                if word not in curr:
                    curr[word] = 1
                else:
                    curr[word] += 1
                if buff >= window:
                    curr[s[hd - wordLen * window:hd - wordLen * (window - 1)]] -= 1
                else: 
                    buff += 1
                if not (goal - curr):
                    res.append(hd - wordLen * (window - 1))
        return res
        