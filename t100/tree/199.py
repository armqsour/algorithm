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