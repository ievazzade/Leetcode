class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append("(")
            elif ch == ")" and len(stack) > 0:
                stack.pop()
            else:
                ans += 1
        
        return ans + len(stack)
        
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        bal = 0
        for ch in s:
            bal += 1 if ch == "(" else -1
            if bal == -1:
                ans += 1
                bal += 1
        
        return ans + bal        