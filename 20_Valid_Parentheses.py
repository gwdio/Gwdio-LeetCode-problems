from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        paren = deque()
        mapping = {'}':'{', ']':'[', ')':'('}
        for c in s:
            if ((c == '(') or (c == '[') or (c == '{')):
                paren.append(c) 
                continue
            if not paren:
                return False
            if paren.pop() != mapping[c]:
                return False
        if paren:
            return False
        return True
        