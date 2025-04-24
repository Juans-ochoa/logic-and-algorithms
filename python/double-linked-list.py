class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        current = self.head
        while current != None:
            print(f'Value: {current.data},', end=' ')
            current = current.next
        print('')

    def insertAtFirst(self, data):
        node = Node(data)

        if self.head == None and self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            node.prev = node
            self.head = node
            node = None
        self.length += 1

    def removeAtFirst(self):
        if self.head == None or self.length == 0:
            return

        removeNode = self.head
        self.head = removeNode.next
        self.head.prev = None

        removeNode.prev = None

        self.length -= 1

        return removeNode.data

    def insertAtLast(self, data):
        if self.head == None and self.length == 0:
            self.insertAtFirst(data)
        else:
            node = Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node = None
            self.length += 1

    def removeAtLast(self):
        if self.head == None:
            return None

        current = self.head
        newTail = None

        while current != None:
            newTail = current
            current = current.next

        if newTail is None:
            self.head = None
            self.tail = None
        else:
            newTail.next = None
            self.tail = newTail

        self.length -= 1

        return current

    def getAtIndex(self, index):
        try:
            if index < 0 or index > self.length:
                raise IndexError('No Node at: '+str(index))
            count = 0
            current = self.head

            while count != index:
                current = current.next
                count += 1

            return current

        except IndexError as err:
            print(f'{err}')

    def insertAtIndex(self, data, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.insertAtFirst(data)
        elif index == self.length - 1:
            self.insertAtLast(data)
        else:
            insertNode = Node(data)
            prevNode = self.getAtIndex(index-1)
            insertNode.next = prevNode.next
            insertNode.prev = prevNode
            prevNode.next = insertNode
            self.length += 1

            return insertNode

    def updateAtIndex(self, data, index):
        try:
            node = self.getAtIndex(index)
            if node != None:
                node.data = data
            else:
                raise IndexError('Node is not found: '+str(index))
        except IndexError as err:
            print(f'{err}')

    def removeAtIndex(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.removeAtFirst()
        elif index == self.length - 1:
            self.removeAtLast()
        else:
            prevNode = self.getAtIndex(index-1)
            tempNode = prevNode.next
            tempNode = tempNode.next
            prevNode.next = tempNode
            tempNode.prev = prevNode

            tempNode = None
            self.length -= 1

            return True


DLL = DoubleLinkedList()
DLL.insertAtFirst(1)
DLL.insertAtFirst(2)
DLL.insertAtLast(5)
DLL.insertAtLast(8)
DLL.insertAtLast(9)
DLL.insertAtIndex(7, 1)
DLL.printList()
DLL.removeAtIndex(3)
DLL.printList()
