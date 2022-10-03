# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from function import get_polynomial
from os import system

k1 = input("Введите степень (k) для первого многочлена: ")
k2 = input("Введите степень (k) для второго многочлена: ")
with open('task5_polynomial_1.txt', 'w') as txtFile:
    txtFile.write(get_polynomial(k1))
with open('task5_polynomial_2.txt', 'w') as txtFile:
    txtFile.write(get_polynomial(k2))

with open('task5_summ_polynomial.txt', 'w') as summ_txt_file:
    with open('task5_polynomial_1.txt', 'r') as txt_file1:
        with open('task5_polynomial_2.txt', 'r') as txt_file2:
            summ_txt_file.write(
                '('+txt_file1.readline()[:-2]+')+('+txt_file2.readline()[:-2]+')')
if input('Сумма многочленов записанна в файл "task5_summ_polynomial.txt". Открыть файл? (Y - да): ') == 'Y':
    system('notepad.exe task5_summ_polynomial.txt')
