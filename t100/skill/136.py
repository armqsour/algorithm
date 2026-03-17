from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for n in nums:
            t ^= n
        return t

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
