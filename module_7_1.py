from pprint import pprint
import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = "product.txt"

    def get_product(self):
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, "r")
            list_of_product = file.read().rstrip()
            file.close()
            return list_of_product
        else:
            print(f"Файл {self.__file_name} не найден.")
            return None

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in self.get_product():
                file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    """Вывод атрибутов объекта p2"""
    print()
    print(p2)  # __str__
    print()
    """Добавление товара в файл product.txt"""
    s1.add(p1, p2, p3)
    print()
    """Чтение файла product.txt"""
    print(s1.get_product())
