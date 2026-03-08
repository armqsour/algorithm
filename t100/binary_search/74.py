from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False