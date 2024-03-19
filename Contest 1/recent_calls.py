from collections import deque

class RecentCounter:

    def __init__(self):
        self.time_queue = deque()
        self.time_window = 3000
        self.total_calls = 0

    def ping(self, t: int) -> int:
        self.total_calls += 1
        if not self.time_queue or self.time_queue[-1][0] < t:
            self.time_queue.append([t, 1])
        else:
            self.time_queue[-1][0] += 1
        
        while self.time_queue[0][0] < t - self.time_window:
            self.total_calls -= self.time_queue.popleft()[1]
        
        return self.total_calls