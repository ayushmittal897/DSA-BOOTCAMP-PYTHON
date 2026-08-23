from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

"""
Approach:
Use a queue (deque) to store the timestamps of pings.
For every new ping `t`, we append it to the queue.
Then, we pop from the front of the queue until all timestamps are within the range `[t - 3000, t]`.
The size of the queue is the number of recent calls.
"""
