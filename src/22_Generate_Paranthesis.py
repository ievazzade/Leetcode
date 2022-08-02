class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
                    
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0
            for ch in A:
                if ch == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        
        ans = []
        generate()
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtracking(openP, closedP):
            if openP == closedP == n:
                res.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backtracking(openP + 1, closedP)
                stack.pop()
                
            if closedP < openP:
                stack.append(")")
                backtracking(openP, closedP + 1)
                stack.pop()
                
        backtracking(0,0)
        return res