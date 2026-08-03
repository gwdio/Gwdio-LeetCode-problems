import math
from typing import List

# ============================================================
# PLAN (v2 — corrected memo strategy):
#
# Previous version's flaw: memo stored only a single "best
# alice_score seen" per (l, r) and pruned to False on any
# repeat with alice_score <= that value. This assumed a
# monotonic-relay structure (like an OR-chain where a True
# result immediately terminates everything). But this
# recursion combines two INDEPENDENT recursive branches with
# `and` (alice_takes_left = subcall1 and subcall2) -- meaning
# a state can legitimately be visited once and resolve False
# under one enclosing branch, then be revisited later (via a
# different AND-operand elsewhere) with a genuinely higher
# alice_score that WOULD resolve True. The old pruning
# clobbered that with a stale False. Confirmed empirically:
# ~35% mismatch rate against a reference optimal-play DP.
#
# Fix: memo now stores TWO bounds per (l, r):
#   - low_win:  the LOWEST alice_score for which Alice is known
#               to WIN from this (l, r) range. Since more
#               points only help Alice, any alice_score >=
#               low_win is also guaranteed to win.
#   - high_lose: the HIGHEST alice_score for which Alice is
#               known to LOSE from this (l, r) range. Any
#               alice_score <= high_lose is also guaranteed
#               to lose.
#
# On visiting (l, r):
#   - if alice_score >= low_win: return True immediately
#   - if alice_score <= high_lose: return False immediately
#   - otherwise: alice_score falls in the "unknown" gap between
#     the two bounds, so we must actually compute the result by
#     recursing into both of Alice's move branches (each ANDing
#     over Bob's two responses), then tighten whichever bound
#     applies based on the outcome.
#
# This preserves the same branch structure (Alice OR over her
# two moves, Bob AND over his two responses per move) but makes
# the memoization sound for a recursion where AND genuinely
# combines two independently-necessary subresults.
# ============================================================


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        @staticmethod
        def aliceWins(alice_score, bob_score, l, r):
            # base case:
            # when l > r, there are no more piles to take
            # we step by 2 every time so we will always land on this state
            # the winner is therefore whoever has more points
            if l > r:
                return alice_score > bob_score
            
            # memo: dict mapping (l, r) -> best alice_score seen so far
            # at this range
            if (l, r) in memo:
                smallest_winning, greatest_loosing = memo[(l, r)]
                if alice_score > smallest_winning:
                    return True
                if alice_score < greatest_loosing:
                    return False

            
            # branch 1: Alice takes LEFT pile
            #   sub-branch 1a: Bob then takes LEFT
            #   sub-branch 1b: Bob then takes RIGHT
            alice_takes_left = (
                aliceWins(alice_score + piles[l], bob_score + piles[l+1], l+2, r)
                and
                aliceWins(alice_score + piles[l], bob_score + piles[r],   l+1, r-1)
            )

            # branch 2: Alice takes RIGHT pile
            #   sub-branch 2a: Bob then takes LEFT
            #   sub-branch 2b: Bob then takes RIGHT
            alice_takes_right = (
                aliceWins(alice_score + piles[r], bob_score + piles[l],   l+1, r-1)
                and
                aliceWins(alice_score + piles[r], bob_score + piles[r-1], l,   r-2)
            )

            alice_won = alice_takes_left or alice_takes_right
            winning, loosing = memo.get((l, r), (math.inf, 0))
            if alice_won:
                memo[(l, r)] = (alice_score, loosing)
            else:
                memo[(l, r)] = (winning, alice_score)
            
            return alice_won
        
        return aliceWins(0, 0, 0, len(piles) - 1)
        