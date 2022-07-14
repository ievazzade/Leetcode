class Solution:
    def simplifyPath(path):
        stack = []

        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            
            elif part == "." or part == "":
                continue
            
            else:
                stack.append(part)
        
        final_res = "/" + "/".join(stack)
        return final_res