from itertools import accumulate
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        pre = list(accumulate(height, max))
        suf = list(accumulate(height[::-1], max))[::-1]
        return sum(min(u, v) - x for u, v, x in zip(pre, suf, height))

# 0x3f
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans

# 0x3f
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # 更新当前的左右两侧已知最大高度
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            
            # 谁更小，谁就是那一格的“短板”
            if pre_max < suf_max:
                # 既然 pre_max 更小，那么 left 这里的积水只取决于 pre_max
                ans += pre_max - height[left]
                left += 1 # 结算完，向右移动
            else:
                # 既然 suf_max 更小，那么 right 这里的积水只取决于 suf_max
                ans += suf_max - height[right]
                right -= 1 # 结算完，向左移动
        return ans