class RPN:

    def __init__(self, expression):
        self.expression = expression

    def check(self):
        tokens = self.expression.split()
        if any(t in ('(', ')') for t in tokens):
            return True
        stack_count = 0
        for token in tokens:
            if token in '+-*/':
                if stack_count < 2:
                    return True
                stack_count -= 1
            else:
                stack_count += 1
        return stack_count != 1

    def postfix(self):
        if not self.check():
            return self.expression
        tokens = self.expression.split()
        output = []
        stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        for token in tokens:
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif token in precedence:
                while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(token)
            else:
                output.append(token)
        while stack:
            output.append(stack.pop())
        return ' '.join(output)

    def calculate(self):
        postfix_expr = self.postfix()
        tokens = postfix_expr.split()
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                res = ""
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = a / b
                stack.append(res)
            else:
                stack.append(float(token))
        return stack[0]
