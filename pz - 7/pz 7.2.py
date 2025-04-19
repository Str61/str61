"""
Дана строка, содержащая латинские буквы и скобки трех видов: «()», «[]», «{}».
Если скобки расставлены правильно (то есть каждой открывающей соответствует
закрывающая скобка того же вида), то вывести число 0. В противном случае вывести
или номер позиции, в которой расположена первая ошибочная скобка, или, если
закрывающих скобок не хватает, число —1
"""


def check_parentheses(s):
    # Стек для хранения открывающих скобок
    stack = []

    for index, char in enumerate(s):
        if char in '([{':
            stack.append((char, index + 1))
        elif char in ')]}':
            # Если стек пуст или верхний элемент стека не соответствует закрывающей скобке
            if not stack:
                return index + 1
            top_char, top_index = stack.pop()
            if (char == ')' and top_char != '(') or (char == ']' and top_char != '[') or (char == '}' and top_char != '{'):
                return index + 1
    # недостаток элементов
    if stack:
        return -1
    # всё верно
    return 0

string_user = str(input("Enter the string: "))
print(f"Program log: {check_parentheses(string_user)}")

