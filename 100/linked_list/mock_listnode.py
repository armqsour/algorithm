class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_linknode(nums):
    if not nums:
        return None
    
    # 1. 创建一个虚拟头节点，它的 next 将指向真正的链表头
    dummy = ListNode(0)
    current = dummy
    
    # 2. 遍历列表，依次创建新节点并链接
    for val in nums:
        current.next = ListNode(val)
        current = current.next
        
    # 3. 返回真正起始的节点
    return dummy.next

def print_listnode(head: ListNode):
    while head:
        print(head.val, end=' ')
        head = head.next