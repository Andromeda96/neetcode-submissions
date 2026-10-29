class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                n1 = stack[-1]
                stack.pop()
                n2 = stack[-1]
                stack.pop()
                if tokens[i] == '+':
                    n3 = n1 + n2
                if tokens[i] == '-':
                    n3 = n2 - n1
                if tokens[i] == '*':
                    n3 = n2*n1
                if tokens[i] == '/':
                    n3 = int(n2/n1)
                    
                stack.append(n3)
        
        return stack[0]