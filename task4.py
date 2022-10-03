# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.


from function import get_polynomial
from os import system

monomial = input("Введите количество одночленов: ")
k = input("Введите степень (k): ")
if (int(k) in range(2, 101)) and (int(monomial) in range(1, 4)):
    my_polynomial=get_polynomial(monomial, k)
    print(f'Многочлен степени k({k}): {my_polynomial}')
    with open('task4.txt', 'w') as txtFile:
        txtFile.write(my_polynomial)
    if input('Многочлен записанн в файл "task4.txt". Открыть файл? (Y - да): ')=='Y':
        system('notepad.exe task4.txt')
else:
    print('Степень числа не в диапазоне от 2 до 100, или количество одночленов не в диапазоне от 1 до 3')
