from typing import List

# 0x3f
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_has_zero = [0 in row for row in matrix]  # 行是否包含 0
        col_has_zero = [0 in col for col in zip(*matrix)]  # 列是否包含 0

        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:  # i 行或 j 列有 0
                    matrix[i][j] = 0  # 题目要求原地修改，无返回值
