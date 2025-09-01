from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        addHead = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[addHead-1]:
                nums[addHead] = nums[i]
                addHead += 1

        return (addHead)