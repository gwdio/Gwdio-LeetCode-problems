from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #do binsearch 2 pointer
        def pprint_lmh(arr, low=None, mid=None, high=None):
            """Pretty print with low/mid/high markers: (low, [mid], high)"""
            parts = []
            for i, val in enumerate(arr):
                s = str(val)
                if i == mid:
                    s = f"[{s}]"
                if i == low:
                    s = f"({s}"
                if i == high:
                    s = f"{s})"
                parts.append(s)
            return ", ".join(parts)


        def pprint_point(arr, idx, label="*"):
            """Pretty print with a single index highlighted, e.g. for longl[p - mid]"""
            parts = []
            for i, val in enumerate(arr):
                if i == idx:
                    parts.append(f"{label}{val}{label}")
                else:
                    parts.append(str(val))
            return ", ".join(parts)


        def pprint_partition(arr, cut):
            """
            Pretty print arr with a partition line inserted right before index `cut`.
            e.g. arr=[1,3,8,9,15], cut=2 -> "1, 3 | 8, 9, 15"
            cut can be <= 0 (partition before everything) or >= len(arr) (partition after everything).
            """
            parts = [str(v) for v in arr]
            cut = max(0, min(cut, len(arr)))
            return ", ".join(parts[:cut]) + " | " + ", ".join(parts[cut:])


        def print_iteration(short, low, mid, high, longl, point_idx, **extra_values):
            """
            Call this once per loop iteration.
            Prints short with (low,[mid],high), longl with the compared index marked,
            the current low/high partition of each array (given current mid guess),
            then a line with any extra values you pass in (p=, low=, hi=, etc).
            """
            print("short:", pprint_lmh(short, low, mid, high))

            if point_idx is not None and 0 <= point_idx < len(longl):
                print("longl:", pprint_point(longl, point_idx))
            else:
                print("longl:", ", ".join(str(v) for v in longl), f"  (index {point_idx} out of range)")

            # eventual partition cut points implied by current mid, per current formulas
            short_cut = mid
            long_cut = point_idx
            print(f"short partition @ cut={short_cut}:", pprint_partition(short, short_cut))
            print(f"longl partition @ cut={long_cut}:", pprint_partition(longl, long_cut))

            vals = {"low": low, "mid": mid, "high": high, "point_idx": point_idx, **extra_values}
            print("  " + ", ".join(f"{k}={v}" for k, v in vals.items()))
            print()


        l1 = len(nums1)
        l2 = len(nums2)
        if l1 <= l2:
            short = nums1
            longl = nums2
            ls = l1
            ll = l2
        else:
            short = nums2
            longl = nums1
            ls = l2
            ll = l1

        p = (l1 + l2) // 2
        low = 0
        hi = ls
        med = hi // 2
        slo = short[:med]
        shi = short[med:]
        llo = longl[:p - med]
        lhi = longl[p - med:]
        while max(self.geth(slo, False), self.geth(llo, False)) > min(self.geth(shi, True), self.geth(lhi, True)):
            # print_iteration(short, low, med, hi, longl, p - med, p=p)
            if self.geth(slo, False) < self.geth(lhi, True):
                low = med
                med = (low + hi + 1) // 2
            else:
                hi = med
                med = (low + hi) // 2
            slo = short[:med]
            shi = short[med:]
            llo = longl[:p - med]
            lhi = longl[p - med:]
            print(f"{slo}|{shi}\n{llo}|{lhi}")
        # print_iteration(short, low, med, hi, longl, p - med, p=p)

       
        print(f"slo: {slo}\nllo: {llo}\nshi: {shi}\nlhi: {lhi}")
        print("final short partition:", pprint_partition(short, med))
        print("final longl partition:", pprint_partition(longl, p - med))
        if (ls + ll) & 1:
            return min(self.getl(shi, False), self.getl(lhi, False))
        return (max(self.getl(slo, True), self.getl(llo, True)) + min(self.getl(shi, False), self.getl(lhi, False))) / 2
    
    def getl(self, l: List[int], low: bool) -> int:
        if not l:
            return -2**31 if low else 2**31
        return l[-1] if low else l[0]

    def geth(self, l: List[int], low: bool) -> int:
        if not l:
            return 2**31 if low else -2**31
        return l[0] if low else l[-1]