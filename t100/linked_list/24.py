from typing import Optional
from mock_listnode import ListNode, list_to_linknode, print_listnode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur0 = dummy = ListNode(0)
        dummy.next = head
        cur1 = head
        while cur1 and cur1.next:
            cur2 = cur1.next
            cur3 = cur1.next.next

            cur0.next = cur2
            cur2.next = cur1
            cur1.next = cur3

            cur0 = cur1
            cur1 = cur3
        return dummy.next

# 0x3f
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 递归边界
            return head  # 不足两个节点，无需交换

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)  # 1 指向递归返回的链表头
        node2.next = node1  # 2 指向 1

        return node2  # 返回交换后的链表头节点
