class myStack:

    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def is_full(self):
        if len(self.data) == 5:
            return True
        else:
            return False

    def push(self, element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return 'overflow'

    def pop(self):
        if len(self.data) == 0:
            return 'underflow'
        else:
            self.data.pop()


a = myStack()
a.push(10)
a.push(23)
a.push(25)
a.push(27)
a.push(11)
print(a.length())
