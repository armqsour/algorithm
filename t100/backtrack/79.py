from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, k):
            # 终止条件：k 到达单词末尾，说明找到了全部字符
            if k == len(word):
                return True
            
            # 越界检查、字符不匹配、或者已经访问过（标记为'#'）
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[k]:
                return False

            # 1. 标记当前格子已访问（防止回头路）
            temp = board[r][c]
            board[r][c] = '#' 

            # 2. 向四个方向递归探索
            # 只要有一个方向返回 True，就说明找到了
            res = (dfs(r + 1, c, k + 1) or 
                   dfs(r - 1, c, k + 1) or 
                   dfs(r, c + 1, k + 1) or 
                   dfs(r, c - 1, k + 1))

            # 3. 回溯：恢复现场，以便其他路径可以再次使用该格子
            board[r][c] = temp
            
            return res

        # 遍历起点
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

print(Solution().exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED"))