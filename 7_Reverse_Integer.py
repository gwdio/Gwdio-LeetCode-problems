import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        negative = x < 0
        if negative:
            x *= -1
        digits = math.floor(math.log10(x))
        sum = 0
        for i in range(digits, -1, -1):
            sum += (x % 10) * 10**i
            x //= 10
        if sum > (2**31 - negative):
            return 0
        if negative:
            return sum * -1
        return sum

        