from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         elif nums[i] + nums[j] == target:
        #             return [i, j]
        res= {}
        for i, n in enumerate(nums):
            if (target - n) in res:
                return [i, res.get(target-n)]
            else:
                res[n] = i