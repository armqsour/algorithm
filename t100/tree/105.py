from typing import List, Optional
from mock_tree import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:1+left_size], inorder[:left_size])
        right = self.buildTree(preorder[1+left_size:], inorder[1+left_size:])
        return TreeNode(preorder[0], left, right)