# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит 
# на экран таблицу умножения всех чисел от 1 до n. 

START = 1
END = 10
n = int(input('Введите число n для таблицы умножения чисел от 1 до n: '))
for i in range(START, END):
    for j in range(START, n  + 1):
        print(f'{j:>2} x {i:>2} = {j * i:>2}', end='    ')
    print('')
