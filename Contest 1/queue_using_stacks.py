class MyQueue:

    def __init__(self):
        self.p = []
        self.q = []

    def push(self, x: int) -> None:
        self.p.append(x)

    def pop(self) -> int:
        self.shift()
        return self.q.pop()

    def peek(self) -> int:
        self.shift()
        return self.q[-1]

    def empty(self) -> bool:
        return not self.p and not self.q

    def shift(self):
        if not self.q:
            while self.p:
                e = self.p.pop()
                self.q.append(e)