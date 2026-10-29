class MinStack:

    def __init__(self):
        self.stack = []
        self.premin = []

    def push(self, val: int) -> None:
        if not self.premin:
            self.premin.append(val)
        elif min(self.premin) > val:
            self.premin.append(val)
        else:
            self.premin.append(self.premin[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.premin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.premin[-1]