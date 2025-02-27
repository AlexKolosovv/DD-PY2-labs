from typing import List, Union
import doctest


class Book:
    def __init__(self, title: str, author: str, year_published: int, pages: int):
        """
        Создание объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param year_published: Год публикации
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.title
        '1984'
        >>> book.pages
        328
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(year_published, int) or year_published <= 0:
            raise ValueError("Год публикации должен быть положительным целым числом")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.year_published = year_published
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        """
        Прочитать указанное количество страниц книги.

        :param pages_to_read: Количество страниц для чтения

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.read(50)
        """
        if not isinstance(pages_to_read, int) or pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным числом")

    def get_info(self) -> str:
        """
        Получить информацию о книге.

        :return: Строка с информацией о книге (название, автор, год публикации)

        Примеры:
        >>> book = Book("1984", "George Orwell", 1949, 328)
        >>> book.get_info()
        '1984, George Orwell, 1949'
        """
        return f"{self.title}, {self.author}, {self.year_published}"


class Car:
    def __init__(self, brand: str, model: str, year: int, fuel_level: float):
        """
        Создание объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска автомобиля
        :param fuel_level: Уровень топлива в автомобиле

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 50.0)
        >>> car.brand
        'Toyota'
        >>> car.fuel_level
        50.0
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год выпуска автомобиля должен быть положительным целым числом")
        if not isinstance(fuel_level, (int, float)) or fuel_level < 0:
            raise ValueError("Уровень топлива должен быть положительным числом или нулем")

        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> None:
        """
        Поехать на автомобиле на определенное расстояние, расходуя топливо.

        :param distance: Расстояние для поездки в километрах

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 50.0)
        >>> car.drive(100)
        """
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        fuel_needed = distance * 0.1  # Пример расхода топлива 0.1 литра на км
        if self.fuel_level < fuel_needed:
            raise ValueError("Недостаточно топлива для поездки")
        self.fuel_level -= fuel_needed

    def refuel(self, fuel: float) -> None:
        """
        Заправить автомобиль.

        :param fuel: Количество топлива для заправки

        Примеры:
        >>> car = Car("Toyota", "Corolla", 2020, 50.0)
        >>> car.refuel(20)
        """
        if not isinstance(fuel, (int, float)) or fuel <= 0:
            raise ValueError("Количество топлива должно быть положительным числом")
        self.fuel_level += fuel


class Computer:
    def __init__(self, brand: str, processor_speed: float, ram_size: int):
        """
        Создание объекта "Компьютер"

        :param brand: Марка компьютера
        :param processor_speed: Скорость процессора в ГГц
        :param ram_size: Размер оперативной памяти в ГБ

        Примеры:
        >>> computer = Computer("Apple", 3.5, 16)
        >>> computer.brand
        'Apple'
        >>> computer.processor_speed
        3.5
        """
        if not isinstance(brand, str):
            raise TypeError("Марка компьютера должна быть строкой")
        if not isinstance(processor_speed, (int, float)) or processor_speed <= 0:
            raise ValueError("Скорость процессора должна быть положительным числом")
        if not isinstance(ram_size, int) or ram_size <= 0:
            raise ValueError("Размер оперативной памяти должен быть положительным целым числом")

        self.brand = brand
        self.processor_speed = processor_speed
        self.ram_size = ram_size

    def run_program(self, program_name: str) -> None:
        """
        Запустить программу на компьютере.

        :param program_name: Название программы

        Примеры:
        >>> computer = Computer("Apple", 3.5, 16)
        >>> computer.run_program("Safari")
        """
        if not isinstance(program_name, str):
            raise TypeError("Название программы должно быть строкой")
        print(f"Запускаем программу: {program_name}")

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Улучшение оперативной памяти.

        :param additional_ram: Количество добавляемой оперативной памяти в ГБ

        Примеры:
        >>> computer = Computer("Apple", 3.5, 16)
        >>> computer.upgrade_ram(8)
        """
        if not isinstance(additional_ram, int) or additional_ram <= 0:
            raise ValueError("Количество добавляемой оперативной памяти должно быть положительным целым числом")
        self.ram_size += additional_ram


if __name__ == "__main__":
    doctest.testmod()
