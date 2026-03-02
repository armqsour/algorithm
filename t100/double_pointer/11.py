from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        ans = min(height[0], height[1]) * 1

        while left < right:
            ans = max((right-left) * min(height[left], height[right]), ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans