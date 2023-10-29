# Выполнение задачи можно разделить по этапам:
# . сначала написать ĸальĸулятор, ĸоторый считывает значения, выводит результат
# и завершает работу
# . затем реализовать REPL
# . после этого реализовать запись истории
# > 1
# > 2
# > +
# 1+2=3
# + ['1+2=3', '3+4=7']
# - []
# / []
# * []

operations = {'+': [], '-': [], '/': [], '*': []}

while True:
    try:
        a = int(input('Введите первое число\n'))
        b = int(input('Введите второе число\n'))
    except ValueError:
        print('Введите десятичное число\n')
        continue

    oper = input('Введите операцию +, -, / или *\n')

    result = 0

    if oper == '+':
        result = a + b
    elif oper == '-':
        result = a - b
    elif oper == '/':
        if b != 0:
            result = a / b
        else:
            print('Делить на 0 нельзя')
            continue
    elif oper == '*':
        result = a * b
    else:
        print('Такой операции нет')
        continue

    result_string = f'{a}{oper}{b}={result}'
    operations[oper].append(result_string)
    print(result_string)

    for key, value in operations.items():
        print(key, value)
