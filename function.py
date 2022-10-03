from math import pi
from random import randint


def get_random_list(len_list, min_list, max_list):
    rand_list = []
    for i in range(0, len_list):
        rand_list.append(randint(min_list, max_list+1))
    return rand_list


def get_pi_specified_accuracy(accuracy):
    return str(pi)[:len(accuracy)]


def get_prime_factors(factors):
    prime_factors_list = []
    for i in range(2, int(factors)+1):
        counter = 0
        for j in range(2, i):
            if i % j == 0:
                counter += 1
        if counter == 0:
            prime_factors_list.append(i)
    return prime_factors_list


def get_non_repeating_elements(elements_list):
    non_repeating_list = []
    for i in elements_list:
        if elements_list.count(i) == 1:
            non_repeating_list.append(i)
    return non_repeating_list


def get_polynomial(degree, number_of_monomials ='3'):
    return {
        number_of_monomials == '1': str(randint(2, 11))+'*X**'+degree+'=0',
        number_of_monomials == '2': str(randint(2, 11))+'*X**'+degree+'+'+str(randint(2, 11))+'*X=0',
        number_of_monomials == '3': str(randint(2, 11))+'*X**'+degree+'+'+str(randint(2, 11))+'*X+'+str(randint(2, 11))+'=0'
    }[True]
