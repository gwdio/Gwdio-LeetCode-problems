class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        # print(nums)
        res = []
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums [i - 1]:
                continue
            j = i+1
            k = len(nums) - 1
            if nums[i] > 0:
                # print(f"nums[{i}] = {nums[i]}. Terminating")
                break
            while j < k:
                if nums[k] < 0:
                    # print(f"nums[{k}] = {nums[k]}. Terminating")
                    break
                tot = nums[i] + nums[j] + nums[k]
                advj = False
                advk = False
                # print(f"sum of indexes {i}, {j}, {k} is {nums[i] + nums[j] + nums[k]}")
                if tot == 0:
                    res.append((nums[i], nums[j], nums[k]))
                    advj = True
                    advk = True
                elif tot < 0:
                    advj = True
                else:
                    advk = True
                if advj:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                if advk:
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
        return res