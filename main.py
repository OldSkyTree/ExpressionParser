import operator

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow}
operators_priority = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}


def execute(reverse_polish):
    stack = []
    for lexeme in reverse_polish:
        if is_number(lexeme):
            stack.append(lexeme)
        else:
            stack.append(operators[lexeme](float(stack.pop(-2)), float(stack.pop())))
    return stack.pop()


def convert_to_reverse_polish_notation(expression):
    lexemes = get_lexemes(expression)
    output = []
    stack = []
    for lexeme in lexemes:
        if is_number(lexeme):
            output.append(lexeme)
        elif lexeme == "(":
            stack.append(lexeme)
        elif lexeme == ")":
            current_lexeme = stack.pop()
            while current_lexeme != "(":
                output.append(current_lexeme)
                current_lexeme = stack.pop()
        elif lexeme in operators_priority:
            while stack and stack[-1] in operators_priority and operators_priority[stack[-1]] >= operators_priority[lexeme]:
                output.append(stack.pop())
            stack.append(lexeme)
    while stack:
        output.append(stack.pop())
    return output


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_lexemes(expression):
    lexemes = []
    i = 0
    while i < len(expression):
        if len(expression) > (i + 1) and expression[i].isdigit() and expression[i + 1] == '.':
            j = i + 2
            while j < len(expression):
                if not expression[j].isdigit():
                    lexemes.append(expression[i:j])
                    i = j - 1
                    break
                j += 1
        elif len(expression) > (i + 1) and expression[i].isdigit() and expression[i + 1].isdigit():
            j = i + 1
            while j < len(expression):
                if j == len(expression) - 1:
                    lexemes.append(expression[i:j + 1])
                    i = j
                    break
                elif not expression[j].isdigit():
                    lexemes.append(expression[i:j])
                    i = j - 1
                    break
                j += 1
        else:
            lexemes.append(expression[i])
        i += 1
    return lexemes


exp = input("Введите выражение: ")
rev_polish = convert_to_reverse_polish_notation(exp)
result = execute(rev_polish)
print("Ответ", result)

# (8+2*5.5)/(1+3*2-4^1)
# 825.5*+132*+41^-/
