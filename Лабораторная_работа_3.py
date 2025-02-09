class Book:
    
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        attrs = ", ".join(f"{key[1:]}={value!r}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages
        
    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not (isinstance(new_pages, int) and new_pages > 0):
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration
        
    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not (isinstance(new_duration, (float, int)) and new_duration > 0):
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(new_duration)
