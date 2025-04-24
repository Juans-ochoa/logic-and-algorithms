class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def size(self): return self.size

    def isEmpty(self): return self.front is None

    def displayQueue(self):
        curr = self.front

        while curr != None:
            print(f'{curr.data}', end=' ')
            curr = curr.next

        print()

    def enQueue(self, data):
        node = Node(data)

        if self.isEmpty():
            self.front = self.rare = node
        else:
            self.rare.next = node
            self.rare = node

        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            return

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1


que = QueueLinkedList()
que.enQueue(3)
que.enQueue(1)
que.enQueue(2)
que.displayQueue()
que.deQueue()
que.displayQueue()
