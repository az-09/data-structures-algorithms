class myQueue:

    def __init__(self):
        self.data = []

    def length(self):
        return len(self.data)

    def enque(self, element):
        if self.length < 5:
            return self.data.append(element)
        else:
            return 'overflow'

    def deque(self):
        if self.length > 0:
            return self.data.pop(0)
        else:
            return 'underflow'