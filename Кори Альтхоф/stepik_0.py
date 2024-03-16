# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def enqueue(self, item):
#         self.s1.append(item)
#
#     def dequeue(self):
#         while len(self.s1) > 1:
#             self.s2.append(self.s1.pop())
#         k = self.s1.pop()
#         while len(self.s2) > 0:
#             self.s1.append(self.s2.pop())
#         return k


def min_list_maker(a_list):
    # a_queue = Queue()
    # min_queue = Queue()
    # k = 0
    # for i in range(len(a_list)):
    #     k += 1
    #     if k >= s:
    #         a_queue.dequeue()
    #         min_queue.dequeue()
    #     a_queue.enqueue(a_list[k])
    #     if (a_list[k] < )
    min_list = []
    for i in range(len(a_list) - 2):
        min_list.append(0)
        if a_list[i] < a_list[i + 1]:
            min_list[i] = a_list[i]
        else:
            min_list[i] = a_list[i + 1]
        if min_list[i] > a_list[i + 2]:
            min_list[i] = a_list[i + 2]
    return min_list


the_list = [1, 2, 3, 10, 15, 4, 22, 11, 11, 9, 6]
min_list_orig = [1, 2, 3, 4, 4, 4, 11, 9, 6]
print(min_list_maker(the_list))
