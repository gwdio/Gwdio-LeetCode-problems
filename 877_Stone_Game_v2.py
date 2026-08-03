from typing import List, Optional


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # dp[l][r] will store the OPTIMAL SCORE DIFFERENTIAL achievable by
        # whichever player currently moves first, restricted to the
        # remaining range piles[l..r]. We don't need to track alice_score
        # and bob_score separately, and we don't need to pass an
        # accumulated diff into the recursion -- the differential
        # "from here on" is a self-contained quantity that doesn't depend
        # on anything that happened before we reached this range.
        #
        # We also don't need a separate Alice/Bob identity flag: whoever's
        # turn it is is fully determined by how many piles have already
        # been removed, which is itself fully determined by (l, r) alone.
        # (Sanity check on this: l + r's parity tracks whose turn it is --
        # e.g. Alice always moves when l + r is odd, Bob when it's even --
        # confirming (l, r) alone is sufficient state with no collisions
        # between Alice-turn and Bob-turn meanings at the same indices.)
        dp: List[List[Optional[int]]] = [[None] * n for _ in range(n)]

        def optimal(l: int, r: int) -> int:
            # BASE CASE: no piles left in this range.
            # There is nothing left to gain or lose, so the differential
            # the current mover can achieve from here is trivially 0.
            if l > r:
                return 0

            if dp[l][r] != None:
                return dp[l][r] # type: ignore

            # RECURSIVE STEP:
            # The current mover has exactly two choices: take piles[l] or
            # piles[r]. Whichever they take, the OTHER player then moves
            # first over whatever range remains. That opponent will also
            # play optimally for themselves -- i.e. they will achieve
            # optimal(remaining range) as THEIR OWN differential.
            #
            # From the current mover's perspective, that means: my gain is
            # (the pile I took) MINUS (whatever differential the opponent
            # locks in for themselves over the rest), since their gain is
            # my loss relative to the total. This is the "negamax" framing:
            # negate the opponent's optimal value to convert it into a
            # cost against me, for both possible moves, and pick the move
            # that maximizes my own result (greedy over the two choices,
            # since each branch already bakes in the opponent's own
            # optimal counter-play).
            op = max((piles[l] - optimal(l + 1, r)),
                     (piles[r] - optimal(l, r - 1)))
            dp[l][r] = op
            return op

        # WPMI (proof that `optimal` always returns the true best
        # achievable differential for whoever moves first in [l, r]):
        #
        # BASE CASE: l > r (empty range).
        #   The only possible "move" is no move at all, so the optimal
        #   (and only) differential is 0. This is trivially correct --
        #   the exit case is optimal by definition since it's the sole
        #   possibility.
        #
        # INDUCTIVE STEP:
        #   Assume optimal(l+1, r) and optimal(l, r-1) already correctly
        #   return the best achievable differential for whoever moves
        #   first in THOSE (strictly smaller) ranges -- this is the
        #   inductive hypothesis, and both are strictly smaller ranges
        #   than [l, r], so the induction is well-founded (range size
        #   strictly decreases toward the l > r base case every step).
        #
        #   Given that hypothesis, the current mover's best move is
        #   exactly: take the pile (left or right) whose value minus the
        #   opponent's now-guaranteed-optimal counter-differential is
        #   largest. Since both candidate moves already assume optimal
        #   play from the opponent thereafter (by the inductive
        #   hypothesis), taking the max of the two fully accounts for
        #   every possible line of optimal play from this point onward.
        #
        #   Therefore optimal(l, r) as computed is correct, completing
        #   the inductive step.
        #
        # By WPMI, optimal(l, r) is correct for all valid (l, r), and in
        # particular for the full range (0, n-1).
        #
        # Alice wins iff the first mover (Alice, since she goes first)
        # can force a strictly positive differential over the whole
        # array.
        return optimal(0, n - 1) > 0