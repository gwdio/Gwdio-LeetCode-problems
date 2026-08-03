import heapq
import itertools
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        count = itertools.count()
        hd = ListNode()
        inc = hd
        for l in lists:
            if l:
                heapq.heappush(heads, (l.val, next(count), l.next))

        while len(heads) > 0:
            val, _, l = heapq.heappop(heads)
            inc.next = ListNode(val)
            inc = inc.next
            if l:
                heapq.heappush(heads, (l.val, next(count), l.next))
        
        return hd.next

