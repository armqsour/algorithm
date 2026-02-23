from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sl = sorted(set(nums))
        max_len= 1
        i = 0
        while i < len(sl):
            tmp_max = 1
            jump_plus = False
            while i + 1 < len(sl):
                if sl[i] + 1 == sl[i+1]:
                    tmp_max += 1
                    max_len = max(tmp_max, max_len)
                    i += 1
                    jump_plus = True
                else:
                    break
            i = i if jump_plus else i + 1
        return max_len

# 0x3f
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        sn = set(nums)
        for u in sn:
            if u - 1 in sn:
                continue
            
            nu = u + 1
            while nu in sn:
                nu += 1
            
            res = max(res, nu - u)
        return res





print(Solution().longestConsecutive([1,0,1,2]))