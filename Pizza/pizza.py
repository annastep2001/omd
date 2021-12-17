import click
import random


class Pizza:
    def __init__(self, name, recipe, pizza_size='L'):
        self.name = name
        self.recipe = recipe
        self.pizza_size = pizza_size

    def show_recipe(self):
        res = '-'
        res += self.name + '\n'
        for key, value in self.recipe.items():
            res += f' {key}: '
            for i, ingred in enumerate(value):
                if i != 0:
                    res += ', '
                res += f'{ingred}'
            res += '\n'
        return res

    def __str__(self):
        return self.name + 'размера ' + self.pizza_size

    def __eq__(self, other: object):
        pass


class Margherita(Pizza):
    def __init__(self, pizza_size='L'):
        self.name = 'Margherita 🧀'
        self.pizza_size = pizza_size
        self.recipe = {'ingredients': ['tomato sauce', 'mozzarella', 'tomatoes']}

    def __dict__(self):
        print('recipe:')
        print(self.recipe)

    def __eq__(self, other):
        if isinstance(other, Margherita):
            return self.pizza_size == other.pizza_size
        return False


class Pepperoni(Pizza):
    def __init__(self, pizza_size='L'):
        self.name = 'Pepperoni 🍕'
        self.pizza_size = pizza_size
        self.recipe = {'ingredients': ['tomato sauce', 'mozzarella', 'pepperoni']}

    def __dict__(self):
        print('recipe:')
        print(self.recipe)

    def __eq__(self, other):
        if isinstance(other, Pepperoni):
            return self.pizza_size == other.pizza_size
        return False


class Hawaiian(Pizza):
    def __init__(self, pizza_size='L'):
        self.name = 'Hawaiian 🍍'
        self.pizza_size = pizza_size
        self.recipe = {'ingredients': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}

    def __dict__(self):
        print('recipe:')
        print(self.recipe)

    def __eq__(self, other):
        if isinstance(other, Hawaiian):
            return self.pizza_size == other.pizza_size
        return False


@click.group()
def cli():
    pass


def log(text):
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            time_sec = random.randint(1, 200)
            print(text.format(str(time_sec)))

        return wrapper

    return decorator


@log('🍽 Приготовили за {} с!')
def bake(pizza: Pizza):
    """Готовит пиццу"""
    print('⏳ Готовим вашу пиццу', pizza)


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('pizza_size', default='L')
def order(pizza: str, pizza_size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza == 'margherita':
        order_pizza = Margherita(pizza_size)
    elif pizza == 'pepperoni':
        order_pizza = Pepperoni(pizza_size)
    elif pizza == 'hawaiian':
        order_pizza = Hawaiian(pizza_size)
    else:
        click.echo('Извините, мы делаем только margherita, pepperoni, hawaiian')
        return

    bake(order_pizza)

    if delivery:
        delivery_pizza(order_pizza)
    else:
        pickup(order_pizza)

    click.echo('Приятного аппетита!')


@log('🚗 Доставили за {} с!')
def delivery_pizza(pizza: Pizza):
    """Доставляет пиццу"""
    print('⏳ Доставляем вашу пиццу', pizza)


@log('🏡 Забрали за {}с!')
def pickup(pizza: Pizza):
    """Самовывоз"""
    print('Можете забрать пиццу', pizza)


@cli.command()
def menu():
    """Показывает меню"""
    click.echo(Margherita().show_recipe())
    click.echo(Pepperoni().show_recipe())
    click.echo(Hawaiian().show_recipe())


if __name__ == '__main__':
    cli()
