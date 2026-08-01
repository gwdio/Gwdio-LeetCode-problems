class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        pot = set()
        @staticmethod
        def matchString(i: int, j: int) -> bool:
            if (i,j) in pot:
                # print(f"s: {s[i:]}, p: {p[j:]} in pot")
                return False
            pot.add((i,j))
            # print(f"s: {s[i:]}, p: {p[j:]} added to pot")
            if j == len(p):
                # print(f"p has terminated, remaining s is {s[i:]}")
                return i == len(s)
            if i == len(s):
                if len(p) - j >= 2 and p[j + 1] == '*':
                    return matchString(i, j+2)
                return False
            matched = p[j]== '.' or s[i] == p[j]
            if len(p) - j >= 2 and p[j + 1] == '*':
                return matchString(i, j+2) or (matched and matchString(i+1, j))
            if not matched:
                # print(f"did not match {s[i]} with {p[j]}")
                return False
            return matchString(i+1, j+1)
        return matchString(0, 0)
            
        