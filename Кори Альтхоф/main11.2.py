class MaxStack:
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return self.max[-1]


a_stack = MaxStack()
a_stack.push(12)
print(a_stack.get_max())
a_stack.push(19)
print(a_stack.get_max())
a_stack.push(20)
print(a_stack.get_max())
a_stack.push(212)
print(a_stack.get_max())
a_stack.pop()
a_stack.push(162)
print(a_stack.get_max())
a_stack.push(12)
print(a_stack.get_max())
a_stack.push(16)
print(a_stack.get_max())
a_stack.push(10)
print(a_stack.get_max())
a_stack.push(22)
print(a_stack.get_max())
a_stack.push(1111)
print(a_stack.get_max())
