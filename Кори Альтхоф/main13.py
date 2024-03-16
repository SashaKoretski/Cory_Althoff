def duplicate_delete(a_line):
    a = a_line.split(" ")
    a_dict = {}
    a_line2 = ""
    for index, word in enumerate(a):
        if word in a_dict:
            continue
        a_dict[word] = index
        a_line2 += word + " "
    return a_line2


the_line = "a a a a the the the a alo aloo alo"
print(duplicate_delete(the_line))
