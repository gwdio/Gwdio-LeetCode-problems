# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = self.addCarry(0, l1, l2)
        if res:
            return res
        return ListNode(0)
    
    def addCarry(self, carry: int, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cr, val = self.sum(carry, l1.val if l1 else 0, l2.val if l2 else 0)
        if not (l1 or l2 or cr or val):
            return None
        return ListNode(val, self.addCarry(cr, l1.next if l1 else None, l2.next if l2 else None))

    def sum(self, cr, v1: int, v2: int) -> Tuple[int, int]:
        if cr + v1 + v2 >= 10:
            return (1, cr + v1 + v2 - 10)
        return (0, cr + v1 + v2)