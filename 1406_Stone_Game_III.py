from typing import List, Optional
import math

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp: List[Optional[int]] = [None] * n

        def score(idx: int) -> int:
            if idx == n:
                return 0
            if dp[idx] is not None:
                return dp[idx] # type: ignore

            best = -math.inf
            running_take = 0
            for take in range(1, min(3, n - idx) + 1):
                running_take += stoneValue[idx + take - 1]
                best = max(best, running_take - score(idx + take))

            dp[idx] = best # type: ignore
            return best # type: ignore

        final = score(0)
        if final > 0: return "Alice"
        elif final < 0: return "Bob"
        else: return "Tie"