class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            if self.sign(dividend) == 1:
                return 2**31 - 1
            else:
                return -2**31
        
        if dividend == -2**31 and divisor == - 1:
            return 2**31 - 1

        res = 0

        sden = self.sign(dividend)
        sdor = self.sign(divisor)

        dividend = abs(dividend)
        divisor = abs(divisor)

        ms = self.msb(dividend) - self.msb(divisor)

        while ms >= 0:
            res = res << 1
            if dividend >= divisor << ms:
                res += 1
                dividend -= divisor << ms
            ms -= 1

        if sden == sdor:
            return res
        else:
            return self.to_signed32(~res + 1)

    def sign(self, x):
        return (x > 0) - (x < 0)

    def msb(self, x):
        b = 0
        while x:
            x = x >> 1
            b += 1
        return b

    def to_signed32(self, x):
        x &= (1 << 32) - 1
        if x & (1 << 31):
            return x - (1 << 32)
        return x