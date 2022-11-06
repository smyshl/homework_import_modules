import random

currencies = ['руб.', '$', '€', '₿', 'теньге', '¥']


def get_employees():

    employees = ['Илон Маск', 'Джеф Безос', 'Марк Цукерберг', 'Билл Гейтс']
    salaries = [10000000, 500000, 300, 80000, 15, 451000, 90000, 3080000, 92580000]

    words = ['зарабатывает', 'зашибает', 'наваривает']

    print('\nПока мы тут сидим, нормальные пацаны зарабатывают нормальные деньги:')

    for employee in employees:
        print(f'{employee} {random.choice(words)} {random.choice(salaries)} {random.choice(currencies)}')

