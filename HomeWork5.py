# Задание 1
from os import name

print('Задание 1')
f_obj = open('python.txt', 'a')
line = input('Введите строку:\n')
while line:
    f_obj.writelines(line + '\n')
    line = input('Введите строку:\n')
    if not line:
        break
f_obj.close()
# Задание 2
print('Задание 2')
with open("python_new.txt", "w") as file:
    line = input('Введите строку:\n')
    while line:
        file.writelines(line + '\n')
        line = input('Введите строку:\n')
        if not line:
            break
with open("python_new.txt", "r") as file:
    content = file.readlines()
    number = 0
    count_lines = 0
    for i in range(len(content)):
        # content = content.split(' ')
        print(f'Кол-во символов {i + 1} - ой строки: {len(content[i].split())}\n')
        count_lines = i + 1
        number = number + len(content[i].split())
    print('Кол-во строк:', count_lines)
    print(f'Общее количество слов:', number)
print('Задание 3')
# Задание 3
with open("salary_file.txt") as file:
    salaries = []
    lines = file.readlines()
    for line in lines:
        lastname, salary = line.split(' ')
        salaries.append(int(salary))
        if int(salary) <= 20000:
            print(line)
print('Средний оклад:', sum(salaries) / len(salaries))
print('Задание 4')
# Задание 4
#rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#file_new = []
with open('file_numbers.txt', encoding='utf-8') as file:
    lines = file.readlines()

with open('file_numbers_new.txt', 'w', encoding='utf-8') as file_2:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        file_2.write(line)
print('Проверьте запись в файл!')
print('Задание 5')
# Задание 5
def summary():
    try:
        with open('file_summary.txt', 'w+') as file:
            line = input('Введите цифры через пробел \n')
            file.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле!')
    except ValueError:
        print('Ошибка типа переменной!')


summary()
print('Задание 6')
# Задание 6
subjects = {}
with open('file_subjects.txt', 'r') as file_sub:
    for line in file_sub:
        subject, lecture, practice, lab = line.split()
        subjects[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subjects}')
