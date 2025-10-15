### Установка зависимостей:
`pip install -r requirements.txt`

### Запуск скрипта (пример):
`python main.py --files data1.csv data2.csv --report average-rating`

### Запуск тестов:
`python -m pytest --cov=. -v`


## Пример работы программы:
#### скриншот запуска скрипта
<img width="1135" height="195" alt="image" src="https://github.com/user-attachments/assets/d9100ea0-4134-47d5-ac02-8668ff0e46ed" />

#### скриншот запуска тестов
<img width="1195" height="477" alt="image" src="https://github.com/user-attachments/assets/b040b9e2-8e30-4192-bd1f-eb7248edadc6" />
|№ | Название теста | Что проверяет |
|----------|----------|----------|
| 1 | `test_average_rating_basic`   | Среднее значение и агрегация по бренду   |
| 2 | `test_average_rating_ignores_invalid_rows`   | Игнорирование пустых и ошибочных строк   |
| 3 | `test_average_rating_sorting`| Правильный порядок сортировки по рейтингу   |
| 4 | `test_average_rating_handles_empty_file`   | Обработка пустого файла   |
