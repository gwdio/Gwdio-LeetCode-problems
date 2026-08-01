class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        signs = {'+', '-'}
        ls = list(s)
        started = False
        pos = True
        res = 0
        for c in ls:
            print(f"c: {c}")
            print(f"res: {res}")
            if not started:
                if c == ' ':
                    continue
                if c in signs:
                    started = True
                    if c == '-':
                        pos = False
                    continue
                if c in digits:
                    started = True
                    res = res * 10 + (ord(c) - 48)
                    continue
                return 0
            if c not in digits:
                break
            res = res * 10 + (ord(c) - 48)
        print(f"res: {res}")
        if not pos:
            res *= -1
            if res < -2**31:
                return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        return res
        
                
            
        
        