# Вычислить число c заданной точностью d

from function import get_pi_specified_accuracy as get_pi

d = input('Введите число d: ')
if 10**-1 >= float(d) >= 10**-10:
    print(f'Число Pi с точностью {d}: {get_pi(d)}')
else:
    print(f'Число d не входит в диапазон 10^(-1) >= d >= 10^(-10)')
