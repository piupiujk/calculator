def main(expression: str):
    # создание списка чисел
    digits = [i for i in range(1, 11)]
    # создание списка знаков
    signs = ['+', '-', '*', '/']
    # у нас должно быть два числа и знак, поэтому проверяем на количество элементов
    if len(expression.split()) != 3:
        return 'Напишите выражение в виде "2 + 2"'
    # берем первое число
    first_digit = expression.split()[0]
    try:
        # проверяем число ли это
        first_digit = int(first_digit)
        # проверяем положительное ли оно
        if first_digit not in digits:
            return 'Введите положительное число от 1 до 10'
    except:
        return 'Введите целое число'
    # берем второе число
    second_digit = expression.split()[2]
    try:
        second_digit = int(second_digit)
        if second_digit not in digits:
            return 'Введите положительное число от 1 до 10'
    except:
        return 'Введите целое число'
    # берем знак
    current_sign = expression.split()[1]
    if current_sign in signs:
        if current_sign == '+':
            return first_digit + second_digit
        elif current_sign == '-':
            return first_digit - second_digit
        elif current_sign == '*':
            return first_digit * second_digit
        elif current_sign == '/':
            # тут перевеодим в целое число по условию задачи
            return int(first_digit / second_digit)
    else:
        return 'Введите одну из арифметических операций "+, -, *, /"'


expression = input('Введите арифметическое выражение (принимаются числа от 1 до 10 и знаки "+, -, *, /":')
print(main(expression))
