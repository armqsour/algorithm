# Definition for singly-linked list.
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tmp = set()
        pivot = headA
        while pivot :
            tmp.add(pivot)
            pivot = pivot.next
        
        pivot = headB
        while pivot :
            if pivot in tmp:
                return pivot
            pivot = pivot.next
        return None
    
# 0x3f
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p