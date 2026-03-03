from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(arr):
    if not arr:
        return None
    
    # 1. 创建根节点并加入队列
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    # 2. 循环处理队列中的父节点
    while queue and i < len(arr):
        node = queue.popleft()
        
        # 3. 挂载左子节点
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # 4. 挂载右子节点
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
        
    return root