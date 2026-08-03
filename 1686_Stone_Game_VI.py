from typing import List, Tuple

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        diffs: List[Tuple[int, int]] = list(zip(aliceValues, bobValues))
        # sort by maximal "swing"
        diffs.sort(key = lambda t: t[0] + t[1], reverse=True)

        alice, bob = zip(*diffs)
        ascore = sum(alice[::2])
        bscore = sum(bob[1::2])
        if ascore > bscore:
            return 1
        elif bscore > ascore:
            return -1
        else:
            return 0

        