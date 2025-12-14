# qa_python

# Проект: Тестирование класса BooksCollector

Проект содержит тесты для класса `BooksCollector`, который реализует функционал управления коллекцией книг.

## Статистика тестирования

- **Всего тестов (pytest):** 21 (16 уникальных тестовых функций)
- **Успешно пройдено:** 21 (100%)
- **Покрытие кода:** 100%
- **Время выполнения:** ~0.05 секунд

### Покрытие кода:
| Файл      | Строк кода | Пропущено | Покрытие |
|-----------|------------|-----------|----------|
| main.py   | 38         | 0         | 100%     |
| tests.py  | 161        | 0         | 100%     |
| **Всего** | **199**    | **0**     | **100%** |

## Список реализованных тестов

### 1. **Метод `add_new_book()`**
- **`test_add_new_book_duplicate_not_added`** — проверка, что дубликат книги не добавляется
- **`test_add_new_book_name_exceeds_40_chars_not_added`** — проверка, что книга с именем длиннее 40 символов не добавляется

### 2. **Метод `set_book_genre()`**
- **`test_set_book_genre_set_three_different_genres`** — параметризованный тест установки трех разных жанров
- **`test_set_book_genre_default_state_is_empty`** — проверка пустого состояния по умолчанию
- **`test_set_book_genre_nonexistent_genre_not_set`** — проверка, что несуществующий жанр не устанавливается

### 3. **Метод `get_book_genre()`**
- **`test_get_book_genre_returns_set_genre`** — параметризованный тест возврата установленного жанра
- **`test_get_book_genre_nonexistent_book_returns_none`** — проверка возврата `None` для несуществующей книги

### 4. **Метод `get_books_with_specific_genre()`**
- **`test_get_books_with_specific_genre_returns_only_books_of_specific_genre`** — проверка возврата книг только указанного жанра

### 5. **Метод `get_books_genre()`**
- **`test_get_books_genre_returns_books_genre_dict`** — проверка возврата полного словаря с книгами разных жанров

### 6. **Метод `get_books_for_children()`**
- **`test_get_books_for_children_returns_books_suitable_for_children`** — проверка возврата книг, подходящих для детей
- **`test_get_books_for_children_returns_empty_list_when_no_child_friendly_books`** — проверка возврата пустого списка, когда нет подходящих книг

### 7. **Метод `add_book_in_favorites()`**
- **`test_add_book_in_favorites_adds_book_to_favorites`** — проверка добавления книги в избранное
- **`test_add_book_in_favorites_does_not_add_duplicate`** — проверка невозможности добавления дубликата в избранное

### 8. **Метод `delete_book_from_favorites()`**
- **`test_delete_book_from_favorites_removes_book_from_favorites_list`** — проверка удаления книги из избранного с сохранением в основной коллекции

### 9. **Метод `get_list_of_favorites_books()`**
- **`test_get_list_of_favorites_books_returns_favorites_list`** — проверка возврата полного списка избранных книг
- **`test_get_list_of_favorites_books_returns_empty_list_no_books_added`** — проверка возврата пустого списка, когда книги не добавлялись в избранное


## Запуск всех тестов:
py -m pytest tests.py -v

## Запуск с измерением покрытия:
py -m pytest tests.py -v --cov=.
