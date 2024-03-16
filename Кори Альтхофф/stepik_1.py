def skobki_checker(a_line):
    stack1 = []
    stack2 = []
    stack3 = []
    stack1_2 = []
    stack2_2 = []
    stack3_2 = []
    i = 1
    for a in a_line:
        if a == "{":
            stack1.append(a)
            stack1_2.append(i)
        if a == "(":
            stack2.append(a)
            stack2_2.append(i)
        if a == "[":
            stack3.append(a)
            stack3_2.append(i)

        if a == "}":
            if len(stack1) == 0:
                return i
            if stack1.pop() != "{":
                return i
            stack1_2.pop()
        if a == ")":
            if len(stack2) == 0:
                return i
            if stack2.pop() != "(":
                return i
            stack2_2.pop()
        if a == "]":
            if len(stack3) == 0:
                return i
            if stack3.pop() != "[":
                return i
            stack3_2.pop()

        i += 1
    if len(stack1_2) != 0:
        return stack1_2.pop()
    if len(stack2_2) != 0:
        return stack2_2.pop()
    if len(stack3_2) != 0:
        return stack3_2.pop()
    return "Success"


the_line = input()
print(skobki_checker(the_line))
