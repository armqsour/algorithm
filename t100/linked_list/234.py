
from typing import Optional
from mock_listnode import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = ans
            ans = cur
            cur = nxt
        return ans

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.middleNode(head)
        head2 = self.reverseList(middle)
        p = head
        q = head2
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
        