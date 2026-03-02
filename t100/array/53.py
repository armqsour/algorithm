from math import inf
from typing import List


# 0x3f
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans