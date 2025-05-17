class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"/", "+", "-", "*"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            
            operand_two, operand_one = stack.pop(), stack.pop()
            print(str(operand_one) +token+ str(operand_two))
            if token == "/":
                stack.append(-(abs(operand_one) / abs(operand_two)) if operand_one * operand_two < 0 else operand_one / operand_two)
            elif token == "*":
                stack.append(operand_one * operand_two)
            elif token == "-":
                stack.append(operand_one - operand_two)
            elif token == "+":
                stack.append(operand_one + operand_two)

        return int(stack.pop())
            