from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = ""
        def dfs(i, c) -> None:
            nonlocal path  # 声明使用外部的 path
            if i == 2 * n:
                if c == 0:
                    ans.append(path)
                return
            
            # 尝试放左括号
            if c < n: # 注意：这里你的原逻辑缺失了左括号上限判断
                path += '('
                dfs(i + 1, c + 1)
                path = path[:-1] # 回溯：删掉最后一个字符
            
            # 尝试放右括号
            if c > 0:
                path += ')'
                dfs(i + 1, c - 1)
                path = path[:-1] # 回溯：删掉最后一个字符
        
        dfs(0, 0)
        return ans
    
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (2*n)
        def dfs(i, c) -> None:
            nonlocal path  # 声明使用外部的 path
            if i == 2 * n:
                if c == 0:
                    ans.append(''.join(path))
                return
            
            # 尝试放左括号
            if c < n: # 注意：这里你的原逻辑缺失了左括号上限判断
                path[i] = '('
                dfs(i + 1, c + 1)
            
            # 尝试放右括号
            if c > 0:
                path[i] = ')'
                dfs(i + 1, c - 1)
        
        dfs(0, 0)
        return ans


print(Solution2().generateParenthesis(1))