import datetime
import random
from application.salary import *
from application.db.people import *


if __name__ == '__main__':

    print('\nПривет!\nЭто занимательная бухгалтерия')
    print('Сегодня', datetime.date.today().strftime("%d.%m.%Y"), 'и пора начинать заниматься делом')

    get_employees()

    print('\nХочешь зарабатывать больше, чем они?')

    currency = random.choice(currencies)

    desired_salary = int(input(f'Введи какую хочешь зарплату в {currency}: '))

    calculated_salary = calculate_salary(desired_salary, currency)

    vsego_word = ' '

    if desired_salary > calculated_salary:
        vsego_word = ' всего '

    print(f'\nОжидания не всегда совпадают с реальностью;)\n'
          f'Хотелось {desired_salary} {currency}, а начислено{vsego_word}{calculated_salary} {currency} )')

    if calculated_salary > 0:
        print('\nПовезло, ты в плюсе)!\nПоздравляю!')
    elif calculated_salary < 0:
        print('\nНачислено столько, что ты теперь в долгах)!\nОтдавай давай)!')
    elif calculated_salary == 0:
        print('\nНу это просто бинго какое-то, монетка встала на ребро)!\nТебе повезло, остаешься при своих)\n'
              'Просто продолжай учить Python)!')

