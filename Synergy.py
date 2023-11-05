print('Введите количество вводимых чисел:')
count = int(input())
countZero = 0
i = 0

while count > 0:
    i += 1
    print('Введите число № {i}:'.format(i = i))
    number = int(input())
    if number == 0: countZero += 1
    count -= 1
print('Всего было введено нулевых значений: {d}'.format(d = countZero))