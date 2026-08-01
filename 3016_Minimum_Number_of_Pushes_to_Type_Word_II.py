from collections import Counter
from itertools import batched

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = batched(sorted(Counter(word).values(), reverse=True), 8)
        res = 0
        w = 1
        for batch in freq:
            res += w * sum(batch)
            w += 1
        return res