import pytest


from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# тест для проверки добавления книг с минимальной (1), нормальной(9) и максимальной(40) валидной длиной названия книги
    @pytest.mark.parametrize('book_name', [
        'Я',
        'Тихий дон',
        'Преступление и наказание: версия текста.'
    ])
    def test_add_new_book_with_names_min_1_normal_9_max_40_length_added_books(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert len(collector.books_genre) == 1
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''

# тест для проверки НЕвозможности добавления дубликата книги
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        book_name = 'Отрочество'

        collector.add_new_book(book_name)

        collector.add_new_book(book_name)

        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ''
        assert len(collector.books_genre) == 1

# тест для проверки НЕвозможности добавления книги с названием размером больше 40 символов (47 символов)
    def test_add_new_book_name_exceeds_40_chars_not_added(self):
        collector = BooksCollector()
        book_name = 'История одного человека, который изменил весь мир вокруг'

        collector.add_new_book(book_name)

        assert book_name not in collector.books_genre
        assert len(collector.books_genre) == 0



# тест для проверки установления жанра книги с валидными вариантами жанров
    @pytest.mark.parametrize('genre', ['Фантастика', 'Комедии', 'Ужасы'])
    def test_set_book_genre_set_three_different_genres(self, genre):
        collector = BooksCollector()
        book_name = '1984'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre[book_name] == genre

# тест для проверки, что у только что добавленной книги жанр по умолчанию равен пустой строке
    def test_set_book_genre_default_state_is_empty(self):
        collector = BooksCollector()
        book_name = 'Вишнёвый сад'

        collector.add_new_book(book_name)
        
        assert collector.books_genre[book_name] == ''

# тест для проверки, что при попытке установления жанра, которого нет в словаре, жанр книги не устанавливается и остаётся равен пустой строке
    def test_set_book_genre_nonexistent_genre_not_set(self):
        collector = BooksCollector()
        book_name = 'Детство'

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Drama')

        assert collector.books_genre[book_name] == ''


# тест для проверки получения жанра книги по её названию
    @pytest.mark.parametrize('book_name, genre', [
        ('Король Лев', 'Мультфильмы'),
        ('Гарри Поттер и философский камень', 'Фантастика'),
        ('Оно', 'Ужасы'),
        ('Преступление и наказание', 'Детективы')
    ])
    def test_get_book_genre_returns_set_genre(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        
        assert collector.get_book_genre(book_name) == genre

# тест для проверки НЕвозможности получения жанра НЕсуществующей книги (не добавляли книгу в словарь)
    def test_get_book_genre_nonexistent_book_returns_none(self):
        collector = BooksCollector()
        
        assert collector.get_book_genre('Мастер и Маргарита') is None


# тест для проверки получения списка книг жанра Мультфильмы
    def test_get_books_with_specific_genre_returns_only_books_of_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('История игрушек')
        collector.set_book_genre('История игрушек', 'Мультфильмы')

        collector.add_new_book('Холодное сердце')
        collector.set_book_genre('Холодное сердце', 'Мультфильмы')

        collector.add_new_book('Код да Винчи')
        collector.set_book_genre('Код да Винчи', 'Детективы')

        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')

        multfilms = collector.get_books_with_specific_genre('Мультфильмы')

        assert len(multfilms) == 3
        assert 'История игрушек' in multfilms
        assert 'Хоббит' not in multfilms

# тест для проверки получения словаря с книгами
    def test_get_books_genre_returns_books_genre_dict(self):
        collector = BooksCollector()
        books = [
            ('Дюна', 'Фантастика'),
            ('1984', 'Фантастика'),
            ('Оно', 'Ужасы'),
            ('Шерлок', 'Детективы'),
            ('Шрек', 'Мультфильмы')
        ]

        for book_name, genre in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        collector.add_new_book('Юность')

        books_genre_dict = collector.get_books_genre()

        assert len(books_genre_dict) == 6
        assert books_genre_dict['Оно'] == 'Ужасы'
        assert books_genre_dict['Шерлок'] == 'Детективы'
        assert books_genre_dict['Юность'] == ''


# тест на проверку получения книг, подходящие детям
    def test_get_books_for_children_returns_books_suitable_for_children(self):
        collector = BooksCollector()
        books = [
            ('Винни-Пух', 'Мультфильмы'),
            ('Хоббит', 'Фантастика'),
            ('Король Лев', 'Мультфильмы'),
            ('12 стульев', 'Комедии'),
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы')
        ]

        for book_name, genre in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
        
        collector.add_new_book('Гроза')

        books_for_children_list = collector.get_books_for_children()

        assert len(books_for_children_list) == 4
        assert 'Винни-Пух' in books_for_children_list
        assert 'Хоббит' in books_for_children_list
        assert 'Оно' not in books_for_children_list
        assert 'Гроза' not in books_for_children_list

# тест для проверки получения пустого списка книг подходящих для детей при попытке добавления в него книг, которые не подходят детям
    def test_get_books_for_children_returns_empty_list_when_no_child_friendly_books(self):
        collector = BooksCollector()
        books = [
            ('Дракула', 'Ужасы'),
            ('Убийство Роджера Экройда', 'Детективы'),
            ('Сияние', 'Ужасы'),
            ('Молчание ягнят', 'Детективы')
        ]

        for book_name, genre in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
        
        books_for_children_list = collector.get_books_for_children()

        assert len(books_for_children_list) == 0
        assert 'Убийство Роджера Экройда' not in books_for_children_list
        assert 'Молчание ягнят' not in books_for_children_list


# тест для проверки добавления книг в Избранное
    def test_add_book_in_favorites_adds_book_to_favorites(self):
        collector = BooksCollector()
        books = [
            ('Марсианин', 'Фантастика'),
            ('Рататуй', 'Мультфильмы'),
            ('Ирония судьбы', 'Комедии'),
            ('Пила', 'Ужасы'),
            ('Десять негритят', 'Детективы')
        ]

        for book_name, genre in books:
            collector.add_new_book(book_name)

        collector.add_book_in_favorites('Рататуй')
        collector.add_book_in_favorites('Пила')
        collector.add_book_in_favorites('Марсианин')

        assert len(collector.favorites) == 3
        assert 'Пила'in collector.favorites
        assert 'Ирония судьбы' not in collector.favorites

# тест для проверки НЕвозможности добавления дубликата книги в Избранное
    def test_add_book_in_favorites_does_not_add_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Десять негритят')

        collector.add_book_in_favorites('Десять негритят')
        collector.add_book_in_favorites('Десять негритят')

        assert len(collector.favorites) == 1
        assert 'Десять негритят'in collector.favorites


# тест для проверки удаления книги из Избранного
    def test_delete_book_from_favorites_removes_book_from_favorites_list(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_new_book('1984')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_book_in_favorites('Властелин колец')
        collector.add_book_in_favorites('1984')

        collector.delete_book_from_favorites('Властелин колец')

        assert len(collector.favorites) == 1
        assert 'Властелин колец' not in collector.favorites
        assert 'Властелин колец' in collector.books_genre
        assert '1984' in collector.favorites


# тест для проверки получения списка Избранное с книгами
    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()
        books = [
            ('Дюна', 'Фантастика'),
            ('Сияние', 'Ужасы'),
            ('Убийство в Восточном экспрессе', 'Детективы'),
            ('Властелин колец', 'Фантастика'),
            ('Чиполлино', 'Мультфильмы')
        ]
        expected_books = []

        for book_name, genre in books:
            collector.add_new_book(book_name)
            collector.add_book_in_favorites(book_name)
            expected_books.append(book_name)

        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        expected_books.append('1984')

        favorite_books = collector.get_list_of_favorites_books()

        for book in expected_books:
            assert book in favorite_books

        assert len(collector.favorites) == 6
        assert len(favorite_books) == len(collector.favorites)
        assert 'Дюна' in collector.favorites
        assert 'Чиполлино' in collector.favorites
        assert 'Хоббит' not in collector.favorites

# тест для проверки получения пустого списка Избранное, когда книги не добавляли в Избранное
    def test_get_list_of_favorites_books_returns_empty_list_no_books_added(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')

        favorite_books = collector.get_list_of_favorites_books()

        assert favorite_books == []
        assert len(favorite_books) == 0
        assert type(favorite_books) is list
        assert favorite_books == collector.favorites
        assert len(collector.favorites) == 0

