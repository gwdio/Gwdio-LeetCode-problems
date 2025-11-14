import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, (i, j)))
        nodes = [False] * len(points)
        nodes[0] = True

        cost = 0
        for _ in range(len(points) - 1):
            temp = []
            for (weight, (a, b)) in edges:
                if nodes[a] ^ nodes[b]:
                    heapq.heappush(temp, (weight, (a, b)))
            (weight, (a, b)) = heapq.heappop(temp)
            cost += weight
            nodes[a] = True
            nodes[b] = True
        return cost
            


        