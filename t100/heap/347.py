from collections import Counter
from typing import List


# 0x3f
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())

        buckets = [[] for _ in range(max_cnt + 1)]
        for x, c in cnt.items():
            buckets[c].append(x)
        
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans