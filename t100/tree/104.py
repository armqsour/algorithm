from typing import List, Optional
from mock_tree import TreeNode



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return max(l_depth, r_depth) + 1

# 0x3f
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            depth += 1
            nonlocal ans
            ans = max(ans, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)
        dfs(root, 0)
        return ans
