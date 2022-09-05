class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_sum = sum(queue[-size:])
        
        return window_sum/min(len(queue), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.size, self.count)

# My Solution
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque([])
        
    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.popleft()
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)