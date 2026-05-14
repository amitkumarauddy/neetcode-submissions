class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            val = None
            if token == '+':
                val = stack.pop() + stack.pop()
            elif token == '*':
                val = stack.pop() * stack.pop()
            elif token == '-':
                right = stack.pop()
                left = stack.pop()
                val = left - right
            elif token == '/':
                right = stack.pop()
                left = stack.pop()
                val = int(left / right)
            else:
                val = int(token)
            stack.append(val)
        
        return stack[0]
                