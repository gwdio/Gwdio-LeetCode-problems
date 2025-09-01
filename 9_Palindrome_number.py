import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Removes all negative numbers
        if (x < 0):
            return False
        if (x < 10):
            return True
        # Determines the length of the number
        intLen = math.floor(math.log(x,10)) + 1
        # Tests each pair of numbers
        for step in range(intLen // 2):
            # Finds the lower digit
            a = (x // 10 ** step) % 10
            # Finds the upper digit
            b = (x // (10 ** (intLen - 1 - step))) % 10
            # If the compared numbers are not the same
            if (a != b):
                return False
        return True
        