from collections import deque
from math import inf
from typing import List, Optional, Tuple
from mock_tree import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            level_length = len(q)
            level_list = []
            for _ in range(level_length):
                node = q.popleft()
                level_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_list[-1])
        return ans

# 0x3f 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            if depth == len(ans):  # 这个深度首次遇到
                ans.append(node.val)
            dfs(node.right, depth + 1)  # 先递归右子树，保证首次遇到的一定是最右边的节点
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans