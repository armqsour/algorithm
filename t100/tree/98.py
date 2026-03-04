from math import inf
from typing import List, Optional, Tuple
from mock_tree import TreeNode

# 0x3f，前序
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValidBST(root, -inf, inf)
    
    def checkValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if not root:
            return True
        x = root.val
        return left < x < right and self.checkValidBST(root.left, left, x) and self.checkValidBST(root.right, x, right)

# 0x3f，中序
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):  # 左
            return False
        if root.val <= self.pre:  # 中
            return False
        self.pre = root.val
        return self.isValidBST(root.right)  # 右

# 0x3f，后序
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf
