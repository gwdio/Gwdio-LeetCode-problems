class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        a = left ^ right
        msb = 0
        while a:
            a >>= 1
            msb += 1
        return (left >> msb) << msb
