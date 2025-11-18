import heapq
from typing import List, Optional

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        edges = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (cost, (i, j)))
        cost = 0
        remaining = len(points) - 1
        dsu = DSU(len(points))
        while remaining != 0:
            w, (a, b) = heapq.heappop(edges)
            ta, tb = dsu.find(a), dsu.find(b)
            if ta == tb:
                continue
            cost += w
            remaining -= 1
            dsu.union(ta, tb)
        return cost

class DSU:
    """
    Represents a DSU supporting the operations of find and union
    Specifically structured to assume some preset number of nodes.
    """
    def __init__(self, numNodes : int):
        self.dsu : List[TreeNode] = [TreeNode(n) for n in range(numNodes)]


    def find(self, node : int):
        """
        Gets the root node for this node and also flattens the tree by reparenting all
        nodes traversed while reaching the root.
        """
        if self.dsu[node].parent != node:
            self.dsu[node].parent = self.find(self.dsu[node].parent)
            # invariant, will never need to care about the number of children this has again
        return self.dsu[node].parent
    

    def union(self, tree1 : int, tree2 : int):
        """
        Unify the two trees into a singular tree.
        Assumes that each tree is represented by a node at most 1 away from the parent.
        Uses the smaller tree as the child
        """
        smaller = None
        bigger = None
        if (self.dsu[self.dsu[tree1].parent].children > self.dsu[self.dsu[tree2].parent].children):
            smaller = self.dsu[tree2]
            bigger = self.dsu[tree1]
        else:
            smaller = self.dsu[tree1]
            bigger = self.dsu[tree2]
        smaller.parent = bigger.parent
        bigger.children += smaller.children

class TreeNode:
    """
    Represents a node in the graph for a DSU
    """
    def __init__(self, parent : int):
        self.parent = parent
        self.children = 0