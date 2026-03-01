
from typing import Optional
from mock_listnode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp = set()
        while head:
            if head in tmp:
                return True
            tmp.add(head)
            head = head.next
        return False
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False