from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0] * numCourses
        # 返回 True 表示找到了环
        def dfs(x: int) -> bool:
            colors[x] = 1  # x 正在访问中
            for y in g[x]:
                # 情况一：colors[y] == 1，表示发生循环依赖，找到了环
                # 情况二：colors[y] == 0，未知，继续递归 y 获取信息
                # 情况三：colors[y] == 2，继续递归 y 只会重蹈覆辙，和之前一样无法找到环
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True  # 找到了环
            colors[x] = 2  # x 完全访问完毕，从 x 出发无法找到环
            return False  # 没有找到环

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False  # 有环
        return True  # 没有环
    
print(Solution().canFinish(2, [[1,0]]))