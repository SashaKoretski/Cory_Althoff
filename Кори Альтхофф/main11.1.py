def skobki_checker(a_line):
    stack1 = []
    stack2 = []
    for a in a_line:
        if a == "{":
            stack1.append(a)
        if a == "(":
            stack2.append(a)
        if a == "}":
            if len(stack1) == 0:
                return False
            stack1.pop()
        if a == ")":
            if len(stack2) == 0:
                return False
            stack2.pop()
    if len(stack2) != 0 or len(stack1) != 0:
        return False
    return True


the_line = "{asfa(a)(11r1)a{af}}{}"
print(skobki_checker(the_line))
