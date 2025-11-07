from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: # can reach end immediately
            return 0
        current = 0
        jumps = 1 # assume you have to make one jump
        while current + nums[current] < len(nums) - 1: # cannot reach end
            maxIndex = 0 # relative to the current head
            currentMax = 0
            for i in range(1, nums[current] + 1): # search all possible jumps
                if i + nums[current + i] > currentMax:
                    maxIndex = i
                    currentMax = i + nums[current + i]
            jumps += 1
            current += maxIndex
        return jumps