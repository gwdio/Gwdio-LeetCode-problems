import heapq
from typing import List, Tuple


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        search = [] # Current head from nodes we have visited to nodes we have not
        cost = 0 # Current cost of it all
        visited = [False] * len(points) # Note that we have not visited any node yet
        visited[0] = True # Note that we start on the first node; thus we visit it.
        self.addNew(0, visited, search, points)
        count = len(points) - 1 # Number of edges we need

        while count != 0:
            (dist, link) = heapq.heappop(search) # Take lowest-cost edge
            if visited[link]: # If edge connects to somewhere we've been, continue
                continue
            cost += dist
            visited[link] = True # Mark node as visited
            self.addNew(link, visited, search, points)
            count -= 1
        return cost

    def dist(self, a : List[int], b : List[int]) -> int:
        """
        Get manhattan distance between two points
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def addNew(self, me : int, visited : List[bool], search : List[Tuple[int, int]], points : List[List[int]]) -> None:
        """
        All all edges from this node to unvisited nodes to min-heap
        An edge is represented as a cost, and the unconnected node it connects to
        Turns out we don't care where the origin is as long as the origin is visited
        """
        for i in range(len(points)):
            if visited[i]: # Been here already
                continue
            heapq.heappush(search, (self.dist(points[me], points[i]), i))
        
