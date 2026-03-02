from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def _rotate_maxtrix(matrix: List[List[int]]):
            return [list(row) for row in zip(*matrix)][::-1]
        ans = []
        row_len = len(matrix)
        i = 0
        while len(matrix) >= 1:
            ans.extend(matrix[0])
            matrix = _rotate_maxtrix(matrix[1:])
            i += 1
        return ans

# 0x3f
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        i = j = di = 0
        for _ in range(m * n):  # 一共走 mn 步
            ans.append(matrix[i][j])
            matrix[i][j] = None  # 标记，表示已经访问过（已经加入答案）
            x, y = i + DIRS[di][0], j + DIRS[di][1]  # 下一步的位置
            # 如果 (x, y) 出界或者已经访问过
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4  # 右转 90°
            i += DIRS[di][0]
            j += DIRS[di][1]  # 走一步
        return ans

# 0x3f
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        size = m * n
        ans = []
        i, j, di = 0, -1, 0  # 从 (0, -1) 开始
        while len(ans) < size:
            dx, dy = DIRS[di]
            for _ in range(n):  # 走 n 步（注意 n 会减少）
                i += dx
                j += dy  # 先走一步
                ans.append(matrix[i][j])  # 再加入答案
            di = (di + 1) % 4  # 右转 90°
            n, m = m - 1, n  # 减少后面的循环次数（步数）
        return ans
