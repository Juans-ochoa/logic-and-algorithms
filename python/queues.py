class Queue(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size <= 0

    def enQueue(self, item):
        try:
            if self.size >= self.limit:
                raise IndexError('Queue Overflow')

            else:
                self.que.append(item)

            if self.front is None:
                self.front = self.rear = 0
            else:
                self.rear = self.size

            self.size += 1

            print('Queue after enQueue: ', self.que)
        except IndexError as err:
            print(err)

    def deQueue(self):
        try:
            if self.size <= 0:
                raise IndexError('Queue Underflow')
            else:
                self.que.pop()
                self.size -= 1

                if self.size == 0:
                    self.front = self.rear = None
                else:
                    self.rear = self.size - 1
                print('Queue after deQueue: ', self.que)

        except IndexError as err:
            print(err)
            return 0

    def queueRear(self):
        if self.rear is None:
            raise IndexError('Sorry, the queue is empty!')
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            raise IndexError('Sorry the queue is empty!')

        return self.que[self.front]

    def size(self): return self.size


que = Queue()
que.enQueue('first')
print('Front: '+que.queueFront())
print('Rear: '+que.queueRear())
que.enQueue('Second')
que.enQueue('Third')
print('Front: '+que.queueFront())
print('Rear: '+que.queueRear())
que.deQueue()
print('Front: '+que.queueFront())
que.deQueue()
print('Rear: '+que.queueFront())
que.deQueue()
que.deQueue()
