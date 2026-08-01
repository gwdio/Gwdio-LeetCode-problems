from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #mid1 = middle of nums1
        #mid2 = middle of nums2
        #if mid1 < mid2, median of upper part of 1 and lower part of 2. repeat.
        #if no mroe list, return middle of other
        
        while nums1 and nums2:
            m1 = self.median(nums1)
            m2 = self.median(nums2)
            print(f"nums1: {nums1}\nm1: {m1}\nnums2: {nums2}\nm2: {m2}")
            if m1 == m2:
                return m1
            cut = len(nums1) // 2 + len(nums2) // 2
            if m1 < m2:
                if cut > len(nums1):
                    return self.median(nums2[len(nums1):])
                elif cut > len(nums2):
                    return self.median(nums1[cut:len(nums1) - (len(nums2) - cut)])
                nums1 = nums1[cut:]
                nums2 = nums2[:len(nums2) - cut]
            else:
                if cut > len(nums1):
                    return self.median(nums2[cut - len(nums1):len(nums2) - cut])
                elif cut > len(nums2):
                    return self.median(nums1[cut:len(nums1) - (len(nums2) - cut)])
                nums1 = nums1[cut:]
                nums2 = nums2[:len(nums2) - cut]
            # if len(nums1) == len(nums2) == 1:
            #     return (m1 + m2) / 2
        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)
        return 0


    def median(self, nums: List[int]) -> float:
        l = len(nums) // 2
        if len(nums) & 1:
            return nums[l]
        else:
            return (nums[l-1] + nums[l]) / 2

    # def cut(self, n1: List[int], n2: List[int], c: int) -> Tuple[List[int], List[int]]:
    #     if c > len(n1):
    #                 return self.median(n2[c - len(n1):len(n2) - c])
    #             else if c > len(n2):
    #                 return self.median(n1[c:len(n1) - (len(n2) - c]))
    #             n1 = n1[c:]
    #             n2 = n2[:len(n2) - c]