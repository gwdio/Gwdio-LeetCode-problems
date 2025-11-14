from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, count in counts.items():
            buckets[count].append(value)
        res = []
        head = len(nums)
        while len(res) < k:
            head -= 1
            if not buckets[head]:
                continue
            res += buckets[head]
        return res # answer is unique so cannot have a case where you will jump over 10 as that means multiple solutions