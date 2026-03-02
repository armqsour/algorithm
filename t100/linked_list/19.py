from collections import defaultdict
from typing import Optional
from mock_listnode import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = head
        count = 0
        tmp = defaultdict(ListNode)
        tmp[-1] = dummy
        while cur:
            tmp[count] = cur
            count += 1
            cur = cur.next
        pre_pivot = tmp[count - n - 1]
        pre_pivot.next = pre_pivot.next.next
        return head
        
# 0x3f
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 由于可能会删除链表头部，用哨兵节点简化代码
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next  # 右指针先向右走 n 步
        while right.next:
            left = left.next
            right = right.next  # 左右指针一起走
        left.next = left.next.next  # 左指针的下一个节点就是倒数第 n 个节点
        return dummy.next