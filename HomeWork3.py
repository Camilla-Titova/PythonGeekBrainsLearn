# Задание 1
def calc_div(*args):
    try:
        arg1 = int(input('Введите числитель:'))
        arg2 = int(input('Введите знаменатель:'))
        res = arg1 / arg2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return "Wrong devider!You can't use zero as a devider"
    return res


print('Результат деления:', round(calc_div(), 2))
# Задание 2
name = input('Введите имя:')
surname = input('Введите фамилию:')
years = int(input('Введите год рождения:'))
city = input('Город проживания:')
email = input('Введите вашу почту:')
phone_number = input('Введите ваш номер телефона:')


def hum_info(name, surname, years, city, email, phone_number):
    return ' '.join([name, surname, str(years), city, email, phone_number])


print(hum_info(name, surname, years, city, email, phone_number))
# Задание 3
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg2 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3
print(my_func(int(input('Первый аргумент:')), int(input('Второй аргумент:')), int(input('Третий аргумент:'))))
# Задание 4
x = int(input('Введите действительное положительное число:'))
y = int(input('Введите целое отрицательное число:'))
def my_function(x, y):
    res = x ** y
    return res
print('Результат:', round(my_function(x,y), 5))
# Задание 5
def sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите число или нажмите Q для выхода:').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма : {sum_res}')
    print(f'Конечная сумма: {sum_res}')
sum()
# Задание 6
def int_func(*args):
    words = input("Введите слово:")
    print(words.title())
    return

int_func()