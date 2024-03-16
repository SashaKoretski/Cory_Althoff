n = int(input("n = "))
list1 = []
for k in range(n + 1):
    list1.append(k)
list1[1] = 0
list2 = []

i = 2
while i <= n:
    if list1[i] != 0:
        list2.append(list1[i])
        for j in range(i, n + 1, i):
            list1[j] = 0
    i += 1

print(list2)
