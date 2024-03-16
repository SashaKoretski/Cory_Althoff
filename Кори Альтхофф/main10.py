class Node:
    def __init__(self, data, next1=None):
        self.data = data
        self.next = next1


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def detect_circle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def __str__(self):
        if not self.detect_circle():
            node = self.head
            my_string = ""
            while node is not None:
                my_string += str(node.data)
                my_string += "\n"
                node = node.next
            return my_string
        return "It's circle!!!"

    def make_it_circle(self, data):
        element = None
        current = self.head
        while current.next:
            if current.data == data:
                element = current
            current = current.next
        current.next = element


my_list = LinkedList()
for i in range(1, 11):
    my_list.append(i)
print(my_list)
print(my_list.detect_circle())

print()

my_list_circle = LinkedList()
for i in range(1, 6):
    my_list_circle.append(i)
my_list_circle.make_it_circle(2)
print(my_list_circle.detect_circle())
print(my_list_circle)
