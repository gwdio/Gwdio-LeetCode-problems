from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i = 0
        j = len(height)-1
        
        while i < j:
            area = max(area, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                if height[i+1] <= height[i]:
                    while height[i+1] <= height[i]:
                        i+=1
                        if i == j: return area
                else: i+=1
            else:
                if height[j-1] <= height[j]:
                    while height[j-1] <= height[j]:
                        j-=1
                        if i == j: return area
                else: j-=1
        return area