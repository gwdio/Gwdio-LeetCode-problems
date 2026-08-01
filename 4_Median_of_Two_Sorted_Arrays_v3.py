from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 <= l2:
            short, longl = nums1, nums2
            ls, ll = l1, l2
        else:
            short, longl = nums2, nums1
            ls, ll = l2, l1

        p = (l1 + l2) // 2
        low = 0
        hi = ls
        med = hi // 2

        slo = short[:med]
        shi = short[med:]
        llo = longl[: p - med]
        lhi = longl[p - med :]

        while max(self.get(slo, True), self.get(llo, True)) > min(self.get(shi, False), self.get(lhi, False)):
            if self.get(slo, True) < self.get(lhi, False):
                low = med
                med = (low + hi + 1) // 2
            else:
                hi = med
                med = (low + hi) // 2
            slo = short[:med]
            shi = short[med:]
            llo = longl[: p - med]
            lhi = longl[p - med :]

        if (ls + ll) & 1:
            return min(self.get(shi, False), self.get(lhi, False))
        return (max(self.get(slo, True), self.get(llo, True)) + min(self.get(shi, False), self.get(lhi, False))) / 2

    def get(self, l: List[int], low: bool) -> int:
        if not l:
            return -(2**31) if low else 2**31
        return l[-1] if low else l[0]