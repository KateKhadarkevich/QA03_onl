# 1. Напишите программу, которая запрашивает у пользователя:

name = input('What is your name? ')  # - его имя (например, "What is your name?")
age = input('How old are you? ')  # - возраст ("How old are you?")
city = input('Where are you live? ')  # - место жительства ("Where are you live?"
# выводим информацию
print('This is', name)
print('It is', age)
print('(S)he lives in', city)

# 2. Напишите программу, которая предлагала бы пользователю решить пример 4 * 100 - 54.
# Потом выводила бы на экран правильный ответ и ответ пользователя. Подумайте, нужно ли здесь преобразовывать строку в число.

user = int(input('Укажите ответ: 4 * 100 - 54 = '))
result = 4 * 100 - 54
if user == result:
    print('Ответ верный')
else:
    print('Ответ', user, 'неверный. Правильный:', result)

# 3. Запросите у пользователя четыре числа. Отдельно сложите первые два и отдельно вторые два. Разделите первую сумму на вторую.
# Выведите результат на экран так, чтобы ответ содержал две цифры после запятой.
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
d = int(input('Введите четвертое число:'))

ab = a + b
cd = c + d
x = ab / cd
print('Результат вычислений=', round(x, 2))