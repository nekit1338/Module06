class Vehicle:
    __COLOR_VARIANTS = ["red", "green", "black"]

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__engine_power = engine_power
        self.__model = model
        self.__color = color

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horse_power(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model(), self.get_horse_power(), self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() in i.lower():
                self.__color = new_color.capitalize()
                return
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    sedan = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
    sedan.print_info()

    sedan.set_color('Pink')
    sedan.set_color('BLACK')
    sedan.set_color('BrOwN')
    sedan.set_color('ReD')
    sedan.owner = 'Vasyok'
    sedan.print_info()
