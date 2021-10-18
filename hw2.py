import csv


def read_file(name: str) -> list:
    """
    Считывает данные из файла name в список словарей file_list
    Входные параметры
    -----------------------
    name: str - название файла, из которого считываем
    Возвращаемое значение
    -----------------------
    file: list - список словарей, считанный из файла
    """
    file = []
    with open(name) as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=';')
        for row in file_reader:
            file.append(row)
    return file


def csv_fork(fork: dict, path: str):
    """
    Записывает данные о вилке зарплат в файл
    Колнки: Департамент, Количество сотрудников, Минимальная, Максимальная, Средняя зарплата
    Входные параметры
    ------------------
    fork: dict - данные о вилке зарплат
    path: str - путь к файлу, в который будет идти запись
    """

    header = ['Департамент', 'Количество сотрудников', 'Минимальная зарплата', 'Максимальная зарплата',
              'Средняя зарплата']
    data = list(fork.items())
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(header)
        for line in data:
            line_wr = list()
            line_wr.append(line[0])
            line_wr += line[1]
            writer.writerow(line_wr)


def print_fork(fork: dict):
    """
    Вывод вилки зарплат для департаментов
    Входные параметры
    -----------------
    fork: dict - данные о вилке зарплат
    """

    end1 = 'a'
    end2 = 'ов'
    for dep, val in fork.items():
        print(f'{dep}:')
        if 2 <= val[0] % 10 <= 4:
            end = end1
        elif val[0] % 10 > 4:
            end = end2
        else:
            end = ''
        print(f'  {val[0]} сотрудник{end}')
        print('    Зарплата:')
        print(f'    - min = {val[1]}')
        print(f'    - max = {val[2]}')
        print(f'    - mean = {val[3]}')


def print_departments(departments: dict):
    """
    Вывод иерархии департаментов
    Входные параметры
    -----------------
    departments: dict - данные о департаменте

    """

    for dep, com in departments.items():
        print(f'{dep}:')
        for c in com:
            print(f'  - {c}')


def department_hierarchy(file: list) -> dict:
    """
    Составление иерархии департамента
    Входные параметры
    ---------------------
    file: list - файл в виде списка словарей
    Возвращаемое значение
    ---------------------
     - departments: dict
        {'департамент': {'отдел_1', 'отдел_2', ...}}
    """
    departments = {}
    for row in file:
        if row['Департамент'] not in departments:
            departments.setdefault(row['Департамент'], set())
        departments[row['Департамент']].add(row['Отдел'])

    return departments


def salary_fork(file: list) -> dict:
    """
    Составление вилки зарплат для департаментов
     Входные параметры
    ---------------------
    file: list - файл в виде списка словарей
    Возвращаемое значение
    ---------------------
     - fork: dict
        {'департамент': ['численность', 'мин зарплата', 'макс зарплата', 'средняя зарплата']}
    """

    fork = {}

    for row in file:
        department = row['Департамент']
        salary = row['Оклад']
        if department not in fork:
            fork.setdefault(department, list())
            fork[department].append(0)
            fork[department].append(int(salary))
            fork[department].append(int(salary))
            fork[department].append(0)
        fork[department][0] += 1
        fork[department][1] = min(fork[department][1], int(salary))
        fork[department][2] = max(fork[department][2], int(salary))
        fork[department][3] += int(salary)

    for key, value in fork.items():
        value[3] /= value[0]

    return fork


def menu():
    """
    Взаимодействие с пользователем
    """
    print('Меню:')
    print('1. Вывод иерархии: департамент и все команды, которые входят в него')
    print(
        '2. Вывод сводного отчёта по департаментам: название, численность, "вилка" зарплат: мин, макс, средняя зарплата')
    print('3. Сохранение сводного отчёта в виде csv-файла')
    print('4. Выход')
    com = input()
    while com != '4':
        if com == '1':
            file = read_file('Corp Summary.csv')
            hierarchy = department_hierarchy(file)
            print_departments(hierarchy)
        elif com == '2':
            file = read_file('Corp Summary.csv')
            salfork = salary_fork(file)
            print_fork(salfork)
        elif com == '3':
            print('Введите путь к файлу, в который хотите сохранить отчет')
            path = input()
            file = read_file('Corp Summary.csv')
            salfork = salary_fork(file)
            csv_fork(salfork, path)
        elif com == '4':
            break
        else:
            print('Ошибка! Введите число от 1 до 4')

        print('\nВведите следующую команду\n')
        com = input()

    print('Работа закончена')


if __name__ == '__main__':
    menu()
