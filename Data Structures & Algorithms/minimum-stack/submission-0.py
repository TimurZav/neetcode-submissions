class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # ← вместо LinkedList!

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Сравниваем с последним минимумом в min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
