import csv


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

    end = ''
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


def department_hierarchy() -> dict:
    """
    Составление иерархии департамента
    Возвращаемое значение
    ---------------------
     - departments: dict
        {'департамент': {'отдел_1', 'отдел_2', ...}}
    """

    departments = {}
    with open("Corp Summary.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        count = 0
        for row in file_reader:
            if count != 0:
                if row[1] not in departments:
                    departments[row[1]] = set()
                departments[row[1]].add(row[2])
            count += 1

    return departments


def salary_fork() -> dict:
    """
    Составление вилки зарплат для департаментов
    Возвращаемое значение
    ---------------------
     - fork: dict
        {'департамент': ['численность', 'мин зарплата', 'макс зарплата', 'средняя зарплата']}
    """

    fork = {}
    with open("Corp Summary.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        count = 0
        for row in file_reader:
            if count != 0:
                if row[1] not in fork:
                    fork[row[1]] = []
                    fork[row[1]].append(0)
                    fork[row[1]].append(int(row[5]))
                    fork[row[1]].append(int(row[5]))
                    fork[row[1]].append(0)
                fork[row[1]][0] += 1
                fork[row[1]][1] = min(fork[row[1]][1], int(row[5]))
                fork[row[1]][2] = max(fork[row[1]][2], int(row[5]))
                fork[row[1]][3] += int(row[5])
            count += 1

        for key, value in fork.items():
            value[3] /= value[0]

    return fork


def user():
    """
    Взаимодействие с пользователем
    """
    print('Меню:')
    print('1. Вывод иерархии: департамент и все команды, которые входят в него')
    print(
        '2. Вывод сводного отчёта по департаментам: название, численность, "вилка" зарплат: мин, макс, средняя зарплата')
    print('3. Сохранение сводного отчёта в виде csv-файла')
    print('4. Выход')
    com = int(input())
    while (com != 4):
        if com == 1:
            print_departments(department_hierarchy())
        if com == 2:
            print_fork(salary_fork())
        if com == 3:
            print('Введите путь к файлу, в который хотите сохранить отчет')
            path = input()
            csv_fork(salary_fork(), path)
        if com == 4:
            break

        print('\nВведите следующую команду\n')
        com = int(input())

    print('Работа закончена')


if __name__ == '__main__':
    user()
