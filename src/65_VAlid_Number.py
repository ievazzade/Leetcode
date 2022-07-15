class Solution:
    def isNumber(self, s: str) -> bool:
        digit = expo = dot = False
        for i, c in enumerate(s):
            if c.isnumeric():
                digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
            elif c in ["e", "E"]:
                if expo or not digit:
                    return False
                expo = True
                digit = False
            elif c == ".":
                if expo or dot:
                    return False
                dot = True
            else:
                return False
        
        return digit