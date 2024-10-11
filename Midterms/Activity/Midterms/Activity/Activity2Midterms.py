class EnhancedQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("THE QUEUE IS EMPTY!!!")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("THE QUEUE IS EMPTY!!!")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return str(self.queue)

    def clear(self):
        self.queue.clear()

    def __str__(self):
        return self.display()

q = EnhancedQueue()
q.enqueue(5)
print("The queue contains:", q)
q.enqueue(3)
print("The queue contains:", q)
print("The length of the queue is:", q.size())
print("Dequeued item:", q.dequeue())
print("Is the queue empty?", q.is_empty())
print("Dequeued item:", q.dequeue())
print("Is the queue empty?", q.is_empty())
try:
    print(q.dequeue())
except IndexError as e:
    print(e)
q.enqueue(7)
print("The queue contains:", q)
q.enqueue(9)
print("The queue contains:", q)
print("The first item in the queue is:", q.peek())
q.enqueue(9)
print("The queue contains:", q)
print("The length of the queue is:", q.size())
print("Dequeued item:", q.dequeue())
print("The final queue is:", q)

print()
print("=========================================")
print()

q.clear()

q.enqueue(5)
q.enqueue(3)
print("Returned value:", q.dequeue())
q.enqueue(2)
q.enqueue(8)
print("Returned value:", q.dequeue())
print("Returned value:", q.dequeue())
q.enqueue(9)
q.enqueue(1)
print("Returned value:", q.dequeue())
q.enqueue(7)
q.enqueue(6)
print("Returned value:", q.dequeue())
print("Returned value:", q.dequeue())
q.enqueue(4)
print("Returned value:", q.dequeue())
print("Returned value:", q.dequeue())