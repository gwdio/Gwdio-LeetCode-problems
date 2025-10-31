from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = dummy
        end = dummy
        for _ in range(n):
            front = front.next
        while front.next is not None:
            front = front.next
            end = end.next
        end.next = end.next.next
        return dummy.next
        
        
        