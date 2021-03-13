# 3. Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

number = (int(input('Реализуем склонение слова «процент» . Введите число от 0 до 20: ')))

if number == 0 or number >= 5:
    print(number, 'процентов')
elif number == 1:
    print(number, 'процент')
elif number >= 2 or number <= 4:
    print(number, 'процента')
    for i in range(20):
        print(number)

print("Выводим все склонения для проверки")

for number_list in range(21):
    if number_list == 0 or number_list >= 5:
        print(number_list, 'процентов')
    elif number_list == 1:
        print(number_list, 'процент')
    elif number_list >= 2 or number_list <= 4:
        print(number_list, 'процента')
