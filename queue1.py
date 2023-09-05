class listQueue:
    def __init__(self):
        self.queue = []

    def _size(self):
        return len(self.queue)  

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if self.is_empty() == False:
            return self.queue[0]
        else:
            raise IndexError("Peek from empty queue")

queue1 = listQueue()

queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)

print("Queue size:", queue1._size())

print("Peek:", queue1.peek())

print("Dequeue:", queue1.dequeue())

print("Queue size after dequeue:", queue1._size())

print("Is empty?", queue1.is_empty())

queue1.enqueue(40)
queue1.enqueue(50)

print("Queue size:", queue1._size())

print("Dequeue:", queue1.dequeue())
