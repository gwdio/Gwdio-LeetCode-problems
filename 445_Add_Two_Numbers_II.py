from typing import Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        hl1, hl2 = self.fill(l1, l2, l1, l2)
        carry, node = self.addCarry(hl1, hl2)
        if carry:
            return ListNode(1, node)
        return node
    def addCarry(self, l1: ListNode, l2: ListNode) -> Tuple[int, ListNode]:
        if not (l1.next and l2.next): #l2 requirement is redundant but for typing
            if (l1.val + l2.val >= 10):
                return 1, ListNode(l1.val + l2.val - 10, None)
            return 0, ListNode(l1.val + l2.val, None)
        carry, node = self.addCarry(l1.next, l2.next)
        if carry + l1.val + l2.val >= 10:
            return 1, ListNode(carry + l1.val + l2.val - 10, node)
        return 0, ListNode(carry + l1.val + l2.val, node)
    
    def fill(self, hl1: ListNode, hl2: ListNode, l1: Optional[ListNode], l2: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
        if l1 and l2:
            return self.fill(hl1, hl2, l1.next, l2.next)
        if l1:
            return self.fill(hl1, ListNode(0, hl2), l1.next, None)
        if l2:
            return self.fill(ListNode(0, hl1), hl2, None, l2.next)
        return (hl1, hl2)
        