from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        leftover = len(nums)
        for i in range(leftover):
            if (i >= leftover):
                break
            if nums[i] == val:
                for j in reversed(range(leftover)):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        break
                    if i == j: break
                    leftover -= 1
                leftover -= 1
        return max(leftover, 0)