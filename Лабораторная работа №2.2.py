BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта Книга
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages
    def __str__(self) -> str:
        """
        Функция, которая возвращает строку с названием книги
        :return: Книга "название_книги"
        """
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        """
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр
        :return: Book(id_=1, name='test_name_1', pages=200)
        """
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books = []):
        """
        Создание и подготовка к работе объекта Библиотека
        :param books: список книг
        """
        self.books = books
    def get_next_book_id(self) -> int:
        """
        Функция, которая возвращает идентификатор для добавления новой книги в библиотеку.
        :return: новый индекс
        """
        if self.books == []:
            return 1
        return self.books[-1].id + 1
    def get_index_by_book_id(self, looking_for: int):
        """
        Функция, которая возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса
        :return: индекс книги в списке
        """
        for v,i in enumerate(self.books):
            if i.id == looking_for:
                return v
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))