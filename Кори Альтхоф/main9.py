n = int(input("n = "))
an_array = range(1, n)
odd_array = [c for c in an_array if c % 2 == 1]
even_array = [c for c in an_array if c % 2 == 0]

the_array = even_array + odd_array
print(the_array)
