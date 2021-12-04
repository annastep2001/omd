END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class ComputerColor:
    def __str__(self) -> str:
        raise ValueError()

    def __repr__(self) -> str:
        pass

    def __eq__(self, o: object) -> bool:
        pass

    def __add__(self, other) -> "ComputerColor":
        pass

    def __mul__(self, other) -> "ComputerColor":
        pass

    def __rmul__(self, other) -> "ComputerColor":
        pass

    def __hash__(self, other) -> int:
        pass


class Color:
    def __init__(self, red, green, blue):
        self.red_level = red
        self.green_level = green
        self.blue_level = blue

    def __str__(self):
        return f'{START};{self.red_level};{self.green_level};{self.blue_level}{MOD}●{END}{MOD}'

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.blue_level == other.blue_level and self.green_level == other.green_level and self.red_level == other.red_level
        return False

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(min(self.red_level + other.red_level, 255), min(self.green_level + other.green_level, 255),
                         min(self.blue_level + other.blue_level, 255))
        raise ValueError('Not a Color')

    def __hash__(self):
        return self.red_level * 1000000 + self.green_level * 1000 + self.blue_level

    def __mul__(self, contrast):
        if contrast < 0 or contrast > 1:
            raise ValueError('Icorrect contrast')
        cl = -256 * (1 - contrast)
        factor = (259 * (cl + 255)) / (255 * (259 - cl))
        new_red = int(factor * (self.red_level - 128) + 128)
        new_green = int(factor * (self.green_level - 128) + 128)
        new_blue = int(factor * (self.blue_level - 128) + 128)
        return Color(min(new_red, 255), min(new_green, 255), min(new_blue, 255))

    __rmul__ = __mul__


class HSBColor(ComputerColor):
    pass


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red_level = 100
    green_level = 149
    blue_level = 237
    Cornflower_blue = Color(red_level, green_level, blue_level)
    print(Cornflower_blue)
    print(Cornflower_blue == Color(100, 149, 237))
    print(Cornflower_blue == Color(100, 0, 0))
    print(Cornflower_blue == 'blue')

    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red + green)

    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    print(red * 0.5)
    print(0.5 * green)

    print_a(red)
