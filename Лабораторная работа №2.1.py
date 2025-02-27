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


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)

    print(list_books)