from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        minHeap = []
        for value, count in counts.items():
            heapq.heappush(minHeap, (count, value))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [value for _, value in minHeap]
