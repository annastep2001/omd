def step3_bar():
    print("Уснула в баре с зонтиком в обнимку")


def step3_no_bar():
    print("В итоге Утка сидела под своим зонтиком всю ночь и смотрела на дождь")


def step2_umbrella():
    print("Зонт был тяжелый, Утке стало лень идти обратно домой")
    print("Остаться ночевать в баре?")
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_bar()
    return step3_no_bar()


def step2_no_umbrella():
    print(
        "Дождь лил как из ведра. Она промокшая вышла из бара. но тут из-за угла выскочил огромный грузовик и переехал ее.")


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
