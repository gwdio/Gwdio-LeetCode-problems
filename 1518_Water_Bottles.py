class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Algorithm:
        Use a greedy algorithm to drink all the bottles possible, keeping track of the number of empty bottles
        Whenever possible, convert empty bottles to full bottles.
        Whenever all the full bottles are empty, then there are no more bottles to be drunk.
        """
        full_bottles: int = numBottles
        empty_bottles: int = 0
        total_bottles: int = 0
        while full_bottles:
            total_bottles += full_bottles
            empty_bottles += full_bottles
            full_bottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
        return total_bottles