from typing import Optional
from mock_tree import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node
        dfs(root)
        return root

# 0x3f
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left = self.invertTree(root.left)  # 翻转左子树
        right = self.invertTree(root.right)  # 翻转右子树
        root.left = right  # 交换左右儿子
        root.right = left
        return root