# Задание 1
a = 5
info = 'Меня зовут Камилла'
years = 18
print(a, info, years)
num = input('Введите число:')
line = input('Введите строку:')
your_year = input('Вам лет:')
your_name = input('Ваше имя:')
print(num, line)
print(your_year, your_name)
# Задание 2
time = int(input('Введите время в секундах:'))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f"Время в формате чч:мм:сс : {hours}:{minutes}:{seconds}")
# Задание 3
n = int(input('Введите число n:'))
total = (n+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))
print('Сумма равна:', total)
# Задание 4
number = abs(int(input('Введите целое положительное число:')))
max_number = number % 10
while number > 0:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    if number == 9:
        print('Максимальное число:9')
        continue
    else:
        print('Максимальное число:', max_number)
        break
# Задание 5
earning = int(input('Введите значение выручки вашей фирмы:'))
cost = int(input('Введите значение издержки вашей фирмы:'))
if earning > cost:
    print('Ваша фирма в этом месяце ушла в прибыль!')
    profit = earning - cost
    profitability_of_earning = profit / earning
    print('Рентабельность выручки составит:', profitability_of_earning)
    number_of_employee = int(input('Введите количество сотрудников фирмы:'))
    profit_per_employee = profit // number_of_employee
    print('Кол-во прибыли в расчете на одного сотрудника:', profit_per_employee)
else:
    print('Ваша фирма в этом месяца ушла в убыток!')
# Задание 6
a = int(input('Введите кол-во км, которые спортсмен пробежал в 1-й день:'))
b = int(input('Введите искомый результат спорсмена в км:'))
day = 1
print(day, '-й день:', a)
while b > a:
    day += 1
    a = a*0.1+a
    print(day, '-й день:', a)
print('на', day, '-й день достиг результата - не менее', b, 'км')
