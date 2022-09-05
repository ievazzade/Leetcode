class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        max_valid = 0
        
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                max_valid = max(max_valid, i - stack[-1])
        return max_valid