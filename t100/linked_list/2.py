from typing import Optional
from mock_listnode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ""
        pivot = 0
        quotient = remainder = 0
        while l1 and l2:
            pivot = l1.val + l2.val + quotient
            quotient, remainder = divmod(pivot, 10)
            sum = str(remainder) + sum
            l1 = l1.next
            l2 = l2.next

        tmp = l1 or l2
        while tmp:
            pivot = tmp.val + quotient
            quotient, remainder = divmod(pivot, 10)
            sum = str(remainder) + sum
            tmp = tmp.next

        sum = str(quotient) + sum if quotient else sum

        sum_list = list(sum)
        cur = None
        for i in sum_list:
            new_node = ListNode(int(i))
            new_node.next = cur
            cur = new_node
        return cur

# 0x3f
class Solution:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:  # 递归边界
            return None

        s = carry
        if l1:
            s += l1.val  # 累加进位与节点值
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next

        # s 除以 10 的余数为当前节点值，商为进位
        return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))

# 0x3f
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1:
                carry += l1.val  # 节点值和进位加在一起
                l1 = l1.next  # 下一个节点
            if l2:
                carry += l2.val  # 节点值和进位加在一起
                l2 = l2.next  # 下一个节点
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点
