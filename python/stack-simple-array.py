class Stack(object):
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, data):
        if len(self.stk) >= self.limit:
            print('Stack overflow')
        else:
            self.stk.append(data)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack underflow')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print('stack underflow')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)


ourStack = Stack(5)
ourStack.push(1)
ourStack.push(2)
ourStack.push(14)
ourStack.push(10)
ourStack.push(12)
ourStack.push(11)
ourStack.push(18)
ourStack.push(9)
print(ourStack.peek())
ourStack.pop()
print(ourStack.peek())
ourStack.pop()
print(ourStack.peek())
