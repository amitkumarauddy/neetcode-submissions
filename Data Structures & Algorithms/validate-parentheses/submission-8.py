class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "}":"{", "]":"["}

        for b in s:
            if stack and b in par:
                if par[b] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
    
        return not stack