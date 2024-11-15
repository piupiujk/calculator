def main(expression: str):
    digits = [i for i in range(11)]
    signs = ['+', '-', '*', '/']
    if len(expression.split()) != 3:
        return 'Напишите выражение в виде "2 + 2"'
    first_digit = expression.split()[0]
    try:
        first_digit = int(first_digit)
        if first_digit not in digits:
            return 'Введите положительное число от 1 до 10'
    except:
        return 'Введите целое число'
    second_digit = expression.split()[2]
    try:
        second_digit = int(second_digit)
        if second_digit not in digits:
            return 'Введите положительное число от 1 до 10'
    except:
        return 'Введите целое число'
    current_sign = expression.split()[1]
    if current_sign in signs:
        if current_sign == '+':
            return first_digit + second_digit
        elif current_sign == '-':
            return first_digit - second_digit
        elif current_sign == '*':
            return first_digit * second_digit
        elif current_sign == '/':
            return int(first_digit / second_digit)
    else:
        return 'Введите одну из арифметических операций "+, -, *, /"'


expression = input('Введите арифметическое выражение (принимаются числа от 1 до 10 и знаки "+, -, *, /":')
print(main(expression))
