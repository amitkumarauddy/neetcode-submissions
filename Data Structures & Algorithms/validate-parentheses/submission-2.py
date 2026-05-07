class Solution:
    def isValid(self, s: str) -> bool:
        
        combo = {")":"(", "}":"{","]":"["}

        stack = []

        for ch in s:
            if ch not in combo:
                stack.append(ch)

            elif stack and combo[ch] == stack[-1]:
                stack.pop()

            else:
                return False
        
        if not stack:
            return True
        else:
            return False