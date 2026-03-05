from collections import deque
from math import inf
from typing import List, Optional, Tuple
from mock_tree import TreeNode, list_to_binary_tree

# 0x3f
class Solution:
    head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head  # 头插法，相当于链表的 root.next = head
        self.head = root  # 现在链表头节点是 root

# 0x3f
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right  # 左子树链表 -> 右子树链表
            root.right = root.left  # 当前节点 -> 左右子树合并后的链表
            root.left = None
        return right_tail or left_tail or root

# morris
# class Solution {
#     public void flatten(TreeNode root) {
#         TreeNode cur=root;
#         while(cur!=null){
#             if(cur.left!=null){
#                 TreeNode predecessor = cur.left;
#                 while(predecessor.right!=null){
#                     predecessor=predecessor.right;
#                 }
#                 predecessor.right=cur.right;
#                 cur.right=cur.left;
#                 cur.left=null;
#             }
#             cur=cur.right;
#         }
#     }
# }

def morrisInorder(root):
    cur = root
    res = []
    
    while cur:
        if cur.left is None:
            # 1. 左边为空，直接访问并转向右边
            res.append(cur.val)
            cur = cur.right
        else:
            # 2. 找到左子树最右节点（前驱节点）
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            
            if pre.right is None:
                # 情况 A: 建立临时连接，继续向左走
                pre.right = cur
                cur = cur.left
            else:
                # 情况 B: 临时连接已存在，说明左边回来的，断开连接，访问当前，向右走
                pre.right = None
                res.append(cur.val)
                cur = cur.right
    return res

print(morrisInorder(list_to_binary_tree([1,2,3,4,5])))