from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # for each k-group, take the ith element, and insert it after the head.
        # manufacture a phantom head
        # to ensure the k-group is big enough must do an initial walk k elements forward
        hd = ListNode(0, head)
        trav = hd
        khd = hd
        ktl = head
        kacc = head
        while trav.next:
            khd = trav
            ktl = trav.next
            scan = ktl
            for _ in range(k - 1):
                scan = scan.next
                if not scan:
                    return hd.next
            # print("List is long enough")
            for _ in range(k - 1):
                # unplug accumulator
                # head next becomes accumulator
                # accumulator next becomes former head next
                # accumulator becomes tl next
                kacc = ktl.next
                ktl.next = kacc.next
                tmp = khd.next
                khd.next = kacc
                kacc.next = tmp
                # print(hd.next)
            trav = ktl
        return hd.next
