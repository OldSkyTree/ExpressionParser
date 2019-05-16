operators = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}


def check_expression(expression):
    pass


def convert_to_reverse_polish_notation(expression):
    lexemes = get_lexemes(expression)
    print(lexemes)
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
        elif lexeme in operators:
            while stack and stack[-1] in operators and operators[stack[-1]] >= operators[lexeme]:
                output.append(stack.pop())
            stack.append(lexeme)
        print("Lexeme", lexeme)
        print("Stack", stack)
        print("Output", output)
        print()
    while stack:
        output.append(stack.pop())
    print(output)
    print(stack)
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
        if (i + 1) < len(expression) and expression[i + 1] == '.':
            j = i + 2
            while j < len(expression):
                if not expression[j].isdigit():
                    lexemes.append(expression[i:j])
                    i = j - 1
                    break
                j += 1
        else:
            lexemes.append(expression[i])
        i += 1
    return lexemes


convert_to_reverse_polish_notation("(8+2*5.5)/(1+3*2-4^1)")
# (8+2*5.5)/(1+3*2-4^1)
# 825.5*+132*+41^-/
