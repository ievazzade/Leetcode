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

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        "lee(t(c)o)de)"
                     ^            
        valid = 0
        stack = []
        list_string = ["l", "e", "e", "(", "t", "(", "c", ")", "o", ")", "d", "e"]
        
        "((("
        """     
        s = list(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)
