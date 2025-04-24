class QueueDynamic(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self): return self.size <= 0

    def resize(self):
        newQue = list(self.que)
        self.limit = 2 * self.limit
        self.que = newQue
        print('Queue was resized!')

    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()

        self.que.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1

        print('Queue after enQueue: ', self.que)

    def deQueue(self):
        try:
            if self.size <= 0:
                raise IndexError('Queue Underflow!')

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
        try:
            if self.rear is None:
                raise IndexError('Sorry, the queue is empty!')

            return self.que[self.rear]
        except IndexError as err:
            print(err)
            return 0

    def queueFront(self):
        try:
            if self.front is None:
                raise IndexError('The Queue is empty!')

            return self.que[self.front]
        except IndexError as err:
            print(err)
            return 0

    def size(self): return self.size


que = QueueDynamic()
que.enQueue('first')
print('Front: ', que.queueFront())
print('Rear: ', que.queueRear())
que.enQueue('second')
print('Front: ', que.queueFront())
print('Rear: ', que.queueRear())
que.enQueue('third')
que.enQueue('four')
que.enQueue('five')
que.enQueue('six')
print('Front: ', que.queueFront())
print('Rear: ', que.queueRear())
que.deQueue()
print('Front: ', que.queueFront())
print('Rear: ', que.queueRear())
