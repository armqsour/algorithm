class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_left = ans_right = 0

        # 奇回文串
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # 循环结束后，s[l+1] 到 s[r-1] 是回文串
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        # 偶回文串
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        return s[ans_left: ans_right]

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # 1. 初始化 dp 表
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True # 单个字符必然是回文
        
        max_len = 1
        start = 0
        
        # 2. 开始填表
        # i 从右往左（降序），j 从左往右（升序）
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i < 3: # 长度为 2 或 3 的情况
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 3. 更新最长回文串的记录
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i
                    
        return s[start : start + max_len]