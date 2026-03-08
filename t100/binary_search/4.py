from typing import List


# 0x3f
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

        m, n = len(a), len(b)
        a = [-inf] + a + [inf]
        b = [-inf] + b + [inf]

        # 枚举 nums1 有 i 个数在第一组
        # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
        i, j = 0, (m + n + 1) // 2
        while True:
            if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
                max1 = max(a[i], b[j])  # 第一组的最大值
                min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
                return max1 if (m + n) % 2 else (max1 + min2) / 2
            i += 1  # 继续枚举
            j -= 1