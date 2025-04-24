class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        if self.head is None:
            print('The list is empty, please add some!')
            return

        else:
            temp = self.head
            while temp.next != None:
                print("Node value is: ", temp.data)
                temp = temp.next

    def insertLast(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

        return newNode

    def removeLast(self):
        if self.head is None:
            return "The list is empty, you can't remove."

        current = self.head
        newTail = None

        while current.next != None:
            newTail = current
            current = newTail.next

        if newTail is None:
            self.head = None
            self.tail = None
        else:
            newTail.next = None
            self.tail = newTail
        self.length -= 1

        return current

    def insertAtFirst(self, data):
        newNode = Node(data)
        if self.head == None and self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

        return newNode

    def removeAtFirst(self):
        if self.head == None and self.length == 0:
            return 'The linked list is empty'

        removeNode = self.head
        self.head = removeNode.next
        removeNode.next = None
        self.length -= 1

        return removeNode.data

    def getAtIndex(self, index):
        try:
            if index < 0 and index >= self.length:
                raise IndexError('No node at: '+str(index))
            count = 0
            current = self.head

            while count != index:
                current = current.next
                count += 1

            return current

        except IndexError as err:
            print(f'{err}')

    def insertAtIndex(self, index, data):
        try:
            insertedNode = None
            if index < 0 and index > self.length:
                raise IndexError("Can't add index: "+str(index))
            if index == 0:
                self.insertAtFirst(data)
            elif index == self.length:
                self.insertLast(data)
            else:
                insertedNode = Node(data)
                prevNode = self.getAtIndex(index-1)
                insertedNode.next = prevNode.next
                prevNode.next = insertedNode
                self.length += 1

            return insertedNode

        except IndexError as err:
            print(f'Error: ', err)

    def updateAtIndex(self, index, data):
        try:
            node = self.getAtIndex(index)
            if node != None:
                node.data = data
                return node
            else:
                raise IndexError('Node is not found: '+str(index))
        except IndexError as err:
            return err

    def removeAtIndex(self, index):
        if index < 0 or index >= self.length or self.length == 0:
            return False

        elif index == 0:
            self.removeAtFirst()
        elif index == self.length - 1:
            self.removeLast()
        else:
            prevNode = self.getAtIndex(index-1)
            tempNode = prevNode.next
            prevNode.next = tempNode.next
            tempNode = None
            self.length -= 1
            return True


listLinked = LinkedList()
