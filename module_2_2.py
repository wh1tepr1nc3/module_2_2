first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)

