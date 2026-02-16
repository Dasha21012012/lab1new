import doctest
from typing import Union


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц
        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        self.current_page = 1

    def open_book(self, page: int) -> None:
        """
        Открыть книгу на определенной странице.
        :param page: Номер страницы для открытия
        :raise ValueError: Если номер страницы меньше 1 или больше общего количества страниц
        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 320)
        >>> book.open_book(50)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть целым числом")
        if page < 1 or page > self.pages:
            raise ValueError(f"Страница должна быть от 1 до {self.pages}")
        ...

    def get_progress(self) -> float:
        """
        Получить прогресс чтения книги в процентах.
        :return: Процент прочитанных страниц
        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 400)
        >>> book.open_book(100)
        >>> book.get_progress()
        25.0
        """
        ...

    def add_bookmark(self, page: int) -> None:
        """
        Добавить закладку на странице.
        :param page: Номер страницы для закладки
        :raise ValueError: Если номер страницы недопустим
        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.add_bookmark(125)
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"
        :param brand: Производитель смартфона
        :param model: Модель смартфона
        :param battery_capacity: Емкость аккумулятора в мАч
        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 3279)
        """
        if not isinstance(brand, str):
            raise TypeError("Производитель должен быть строкой")
        if not brand.strip():
            raise ValueError("Производитель не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model.strip():
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.battery_capacity = battery_capacity
        self.battery_level = 100
        self.is_on = False

    def turn_on(self) -> None:
        """
        Включить смартфон.
        :raise RuntimeError: Если смартфон уже включен или разряжен
        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 3900)
        >>> phone.turn_on()
        """
        ...

    def charge_battery(self, minutes: int) -> None:
        """
        Зарядить аккумулятор смартфона.
        :param minutes: Время зарядки в минутах
        :raise ValueError: Если время зарядки отрицательное
        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 5000)
        >>> phone.charge_battery(30)
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть целым числом")
        if minutes < 0:
            raise ValueError("Время зарядки не может быть отрицательным")
        ...

    def take_photo(self) -> None:
        """
        Сделать фотографию на камеру смартфона.
        :raise RuntimeError: Если смартфон выключен
        Примеры:
        >>> phone = Smartphone("Google", "Pixel 7", 4355)
        >>> phone.turn_on()
        >>> phone.take_photo()
        """
        ...
class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Стакан"
        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости
        """
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def is_glass(self) -> bool:
        """
        Функция которая проверяет является ли словарь стаканом
        :return: Является ли объект стаканом или нет
        """
        ...

    def add_water_to_glass(self, water: int) -> int:
        """
        Добавление воды в стакан.
        Если количество добавляемой жидкости превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемой жидкости
        :return: Объем непоместившейся жидкости
        """
        ...

    def remove_water_from_glass(self, estimate_water: int) -> int:
        """
        Извлечение воды из стакана
        Если количество извлекаемой жидкости превышает количество воды в стакане,
        то возвращается реальное количество извлеченной воды
        :param estimate_water: Объем извлекаемой жидкости
        :return: Объем реально извлеченной жидкости
        """
        ...


if __name__ == "__main__":
    glass = Glass(500, 0)  # инициализация экземпляра класса        
