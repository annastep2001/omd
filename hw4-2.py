import json


class ColorizeMixin:
    def __init__(self):
        self.repr_color_code = 33


class Advert(ColorizeMixin):
    def __init__(self, description: dict):
        super().__init__()
        for key, value in description.items():
            if type(value) is dict:
                self.__dict__[key] = Advert(value)
            else:
                self.__dict__[key] = value

        if 'price' not in self.__dict__:
            self.__dict__['price'] = 0
        if self.__dict__['price'] < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};49m {self.title} | {self.price} ₽'


if __name__ == "__main__":
    lesson_str = """{
       "title": "iPhone X",
       "price" : 100,
       "location": {
       "address": "город Москва, Лесная, 7",
       "metro_stations": ["Белорусская"]
       }
       }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad)
