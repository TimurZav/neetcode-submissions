import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if not tokens:
            return 0

        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                stack.append(int(operators[token](stack.pop(-2), stack.pop(-1))))
        return stack[0]