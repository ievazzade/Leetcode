class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def numValidParanthesis(s):
            stack = []
            count = 0
            for ch in s:
                if ch == "(":
                    stack.append("(")
                if ch == ")" and stack and stack[-1] == "(":
                    stack.pop()
                    count += 1
            return count
        
        num_valid = numValidParanthesis(s)
        valid_string = []
        stack = []
        for ch in s:
            if ch.isalnum():
                valid_string.append(ch)
            if ch == "(" and num_valid > 0:
                valid_string.append(ch)
                stack.append("(")
                num_valid -= 1
            if ch == ")" and stack and stack[-1] == "(":
                valid_string.append(ch)
                stack.pop()
        return "".join(valid_string)