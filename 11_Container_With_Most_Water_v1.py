from typing import List, Tuple
class Solution:
    def maxArea(self, height: List[int]) -> int:
        cleaned = self.clean(height)
        area = 0
        for i in range((len(cleaned) - 1)):
            for j in range(i, len(cleaned)):
                area = max(area, min(cleaned[i][0], cleaned[j][0]) * (cleaned[j][1] - cleaned[i][1]))
        return area

    def clean(self, hmap: List[int]) -> List[Tuple[int, int]]:
        for i in range(len(hmap)):
            hmap[i] = (hmap[i], i)
        
        i = 0
        l = len(hmap)
        while i < l:
            if (i-1 >= 0) and (i+1 < l) and hmap[i][0] <= hmap[i-1][0] and hmap[i][0] <= hmap[i+1][0]:
                del hmap[i]
                l -= 1
                i -= 1
            else:
                i += 1
        
        return hmap

        