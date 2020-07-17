class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.cur = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.cur = 0
        else:
            self.storage[self.cur] = item
            self.cur = (self.cur+1) % self.capacity
            if len(self.storage) > self.capacity:
                self.storage.pop()

    def get(self):
        return self.storage
