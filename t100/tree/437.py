from collections import deque
from math import inf
from typing import List, Optional, Tuple
from mock_tree import TreeNode

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(root: Optional[TreeNode], targetSum:int) -> int:
            if not root:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += dfs(root.left, targetSum - root.val)
            ret += dfs(root.right, targetSum-root.val)
            return ret
        ret = dfs(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

# 0x3f
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # key：从根到 node 的节点值之和
        # value：节点值之和的出现次数
        # 注意在递归过程中，哈希表只保存根到 node 的路径的前缀的节点值之和
        cnt = defaultdict(int)  
        cnt[0] = 1
        ans = 0

        # s 表示从根到 node 的父节点的节点值之和（node 的节点值尚未计入）
        def dfs(node: Optional[TreeNode], s: int) -> None:
            if node is None:
                return

            nonlocal ans
            s += node.val
            # 把 node 当作路径的终点，统计有多少个起点
            ans += cnt[s - targetSum]

            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1  # 恢复现场（撤销 cnt[s] += 1）

        dfs(root, 0)
        return ans