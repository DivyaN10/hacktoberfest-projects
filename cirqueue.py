class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        
        if self.is_empty():
            self.front = 0  # Initialize front if the queue was empty

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        
        item = self.queue[self.front]
        if self.front == self.rear:  # Queue is now empty after this dequeue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        
        i = self.front
        print("Queue elements: ", end="")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

if __name__ == "__main__":
    cq = CircularQueue(5)

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.display()

    cq.dequeue()
    cq.display()

    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    cq.display()

    cq.dequeue()
    cq.enqueue(7)
    cq.display()
