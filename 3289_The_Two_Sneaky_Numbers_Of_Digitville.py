from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # nums = sorted(nums)
        # print(nums)
        # criminals = []
        # prev = -1
        # for num in nums:
        #     if prev == num:
        #         criminals.append(num)
        #     prev = num
        # return criminals
        counts = [False] * 101
        criminals = []
        for num in nums:
            if counts[num]:
                criminals.append(num)
                if len(criminals) == 2:
                    break
            else:
                counts[num] = True
        return criminals