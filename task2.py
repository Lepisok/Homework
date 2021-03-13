# 1)Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# 2)Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# 3)К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Внимание: новый список не создавать!!!

# 1)Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# numbers = [x**3 for x in range(1, 1000 , 2)] # взял из книги Лунц М.
# print(numbers)

numbers = []

for number_cube in range(1, 1000, 2):
    number = number_cube ** 3
    numbers.append(number)

print(numbers)
# 2)Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
sum = 0
i = 0

for number_del in numbers:
    result = 0
    a = number_del
    while a > 0:
        result += a % 10
        a //= 10
        numbers[i] = result
    if (result % 7) == 0:
        sum += number_del
    i = i + 1

print(sum)

# Прибавить 17 без создания нового списка не получается.
numbers = []

for number_cube in range(1, 1000, 2):
    number = number_cube ** 3
    numbers.append(number)

sum = 0
i = 0
for adding in range(len(numbers)):
    numbers[adding] += 17

for number_again in numbers:
    result = 0
    a = number_again
    while a > 0:
        result += a % 10
        a //= 10
        numbers[i] = result
    if (result % 7) == 0:
        sum += number_again
        i = i + 1

print(sum)

