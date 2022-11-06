import time
import random


def calculate_salary(salary, currency):

    calculated_salary = 0

    for delta_t in range(1, 2001):
        print('\rНачисляю...', calculated_salary, currency, end='')
        time.sleep(0.005)
        calculated_salary += random.randint(-130, 132)
    print()

    return calculated_salary

