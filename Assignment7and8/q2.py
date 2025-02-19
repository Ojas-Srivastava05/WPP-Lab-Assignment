class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def display(self):
        print(self.queue)