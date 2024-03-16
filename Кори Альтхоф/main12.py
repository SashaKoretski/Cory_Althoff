class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        k = self.s1.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return k


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
for i in range(3):
    print(q.dequeue())
