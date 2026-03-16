class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 创建二维 dp 表，大小为 m x n
        # 初始化为 0，或者初始化为 1 会更省事
        dp = [[0] * n for _ in range(m)]
        
        # 2. 初始化边界
        # 第一列的所有格子：只能从上面走下来，所以路径数都是 1
        for i in range(m):
            dp[i][0] = 1
        # 第一行的所有格子：只能从左边走过来，所以路径数都是 1
        for j in range(n):
            dp[0][j] = 1
            
        # 3. 填表：根据转移方程 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # 4. 返回右下角的值
        return dp[m - 1][n - 1]