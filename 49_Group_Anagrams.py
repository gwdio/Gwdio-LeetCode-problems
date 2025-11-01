from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}
        for s in strs:
            sort = "".join(sorted(s))
            if lists.get(sort):
                lists.get(sort).append(s)
            else:
                lists[sort] = [s]
        return list(lists.values())
        