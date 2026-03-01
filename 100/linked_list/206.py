# Definition for singly-linked list.
from typing import Optional
from mock_listnode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        tmp = []
        pivot = head
        while pivot:
            tmp.append(pivot)
            pivot = pivot.next
        n = len(tmp)
        ans = tmp[-1]
        pivot = ans
        for i in range(n-2, -1, -1):
            pivot.next = tmp[i]
            pivot = tmp[i]
        pivot.next = None
        return ans

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = ans
            ans = cur
            cur = nxt
        return ans