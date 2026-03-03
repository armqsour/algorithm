from collections import deque
from typing import List, Optional
from mock_tree import TreeNode, list_to_binary_tree

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])
        while q:
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
            
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                    
            ans.append(current_level)

        return ans

print(Solution().levelOrder(list_to_binary_tree([1,2,3,4,5])))