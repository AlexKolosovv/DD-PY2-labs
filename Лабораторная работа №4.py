class City:
    """
    Базовый класс для всех городов.
    
    Атрибуты:
    name: Название города.
    population: Население города.
    country: Страна, в которой находится город.
    
    Методы:
    __init__(self, name: str, population: int, country: str): Инициализирует объект города.
    __str__(self): Возвращает строковое представление города (название, население, страна).
    __repr__(self): Возвращает официальное строковое представление объекта города.
    """
    
    def __init__(self, name: str, population: int, country: str) -> None:
        """
        Инициализирует объект города с его названием, населением и страной.
        
        :param name: Название города.
        :param population: Население города.
        :param country: Страна, в которой находится город.
        """
        self.name = name
        self.population = population
        self.country = country
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление города.
        
        :return: Строка с названием города, населением и страной.
        """
        return f"Город {self.name}, население: {self.population} человек, страна: {self.country}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление города.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"City(name='{self.name}', population={self.population}, country='{self.country}')"


class Capital(City):
    """
    Класс для представления столицы, наследуется от класса City.
    
    Дополнительный атрибут:
    is_capital: Признак того, является ли город столицей.
    
    Перегруженные методы:
    __str__(self): Представление столицы с указанием, что это столица.
    __repr__(self): Официальное строковое представление столицы.
    
    Расширенные методы:
    famous_landmarks(self): Методы для отображения известных достопримечательностей столицы.
    """
    
    def __init__(self, name: str, population: int, country: str, is_capital: bool) -> None:
        """
        Инициализирует объект столицы, расширяя атрибуты базового класса City.
        
        :param name: Название города.
        :param population: Население города.
        :param country: Страна, в которой находится город.
        :param is_capital: Признак того, является ли город столицей.
        """
        super().__init__(name, population, country)
        self.is_capital = is_capital
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление столицы с указанием, что это столица.
        
        :return: Строка с названием города, населением, страной и статусом столицы.
        """
        capital_status = "Это столица" if self.is_capital else "Не столица"
        return f"Город {self.name}, население: {self.population} человек, страна: {self.country}. {capital_status}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление столицы.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"Capital(name='{self.name}', population={self.population}, country='{self.country}', is_capital={self.is_capital})"
    
    def famous_landmarks(self) -> str:
        """
        Возвращает список известных достопримечательностей столицы.
        
        :return: Строка с примерами достопримечательностей.
        """
        if self.is_capital:
            return f"Известные достопримечательности в {self.name}: памятник независимости, центральная площадь."
        return "Это не столица, достопримечательности не указаны."
        

class PortCity(City):
    """
    Класс для представления портового города, наследуется от класса City.
    
    Дополнительный атрибут:
    port_size: Размер порта (малый, средний, большой).
    
    Перегруженные методы:
    __str__(self): Представление портового города с указанием размера порта.
    __repr__(self): Официальное строковое представление портового города.
    
    Расширенные методы:
    port_activity(self): Информация о деятельности в порту.
    """
    
    def __init__(self, name: str, population: int, country: str, port_size: str) -> None:
        """
        Инициализирует объект портового города, расширяя атрибуты базового класса City.
        
        :param name: Название города.
        :param population: Население города.
        :param country: Страна, в которой находится город.
        :param port_size: Размер порта (малый, средний, большой).
        """
        super().__init__(name, population, country)
        self.port_size = port_size
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление портового города с указанием размера порта.
        
        :return: Строка с названием города, населением, страной и размером порта.
        """
        return f"Город {self.name}, население: {self.population} человек, страна: {self.country}, порт: {self.port_size}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление портового города.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"PortCity(name='{self.name}', population={self.population}, country='{self.country}', port_size='{self.port_size}')"
    
    def port_activity(self) -> str:
        """
        Возвращает информацию о деятельности в порту.
        
        :return: Строка с видом деятельности в порту.
        """
        if self.port_size == 'большой':
            return f"В порту города {self.name} активно развиваются международные морские перевозки."
        elif self.port_size == 'средний':
            return f"В порту города {self.name} развиваются как международные, так и региональные перевозки."
        else:
            return f"В порту города {self.name} сосредоточены местные перевозки."
