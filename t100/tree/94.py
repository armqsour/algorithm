from typing import List, Optional
from mock_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        ans = []
        dfs(root)
        return ans