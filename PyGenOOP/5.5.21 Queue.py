class Queue:
    def __init__(self, *args: tuple):
        self.queue: list = list(args)

    def add(self, *args: list):
        self.queue += args

    def pop(self):
        if self.queue:
            elem = self.queue.pop(0)
            return elem
        return None

    def __str__(self):
        return " -> ".join(map(str, self.queue))

    def __eq__(self, other):
        return self.queue == other.queue

    def __add__(self, other):
        if isinstance(other, Queue):
            new_queue = Queue(*(self.queue + other.queue))
            return new_queue
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue += other.queue
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.queue) <= other:
                return Queue()
            elif len(self.queue) > other:
                return Queue(*self.queue[other:])
        return NotImplemented
