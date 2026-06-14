class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d1 = {")":"(","}":"{","]":"["}

        for i in s:
            if i in d1:
                if stack and d1[i] == stack[-1]:
                    stack.pop()
                else:                    
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False