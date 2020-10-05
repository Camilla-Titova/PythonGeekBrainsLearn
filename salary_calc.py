def sal_calc():
    try:
        time = float(input('Вырабатка в часах:'))
        salary = int(input('Ставка:'))
        bonus = int(input('Премия:'))
        res = time * salary + bonus
        print(f'Заработанная плата сотрудника: {res}')
    except ValueError:
        return print('Вы ввели не число')


sal_calc()
