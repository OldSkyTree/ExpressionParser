import operator
import re
import argparse

operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow}
operators_priority = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.file:
        with open(namespace.file, "r") as file:
            exp = file.readline()
    elif namespace.expression:
        exp = namespace.expression
    else:
        exp = input("Enter expression: ")
    rev_polish_note = reverse_polish_notation(exp)
    print("Answer: ", execute(rev_polish_note))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", nargs="?")
    parser.add_argument('-f', "--file")

    return parser


def check_expression(expression):
    input_string = str(expression)
    input_string.replace(" ", "")
    if "," in input_string:
        raise ValueError()


def execute(reverse_polish):
    stack = []
    for lexeme in reverse_polish:
        if is_number(lexeme):
            stack.append(lexeme)
        else:
            stack.append(operators[lexeme](float(stack.pop(-2)), float(stack.pop())))
    return stack.pop()


def reverse_polish_notation(expression):
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
            while stack and stack[-1] in operators_priority and \
                    operators_priority[stack[-1]] >= operators_priority[lexeme]:
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
        number = re.match(r"[0-9]+\.*[0-9]+", expression[i:])
        if number:
            lexemes.append(number.group())
            i += number.end() - 1
        else:
            lexemes.append(expression[i])
        i += 1
    return lexemes


if __name__ == "__main__":
    main()
