## TODO DRF

Запуск стандартный:
python manage.py runserver

База sqlite, файл БД с готовым наполнением приложил.

Все API по заданию:
GET /api/tasks - получть список всех задач
GET /api/tasks/{id} - получть одну конкретную задачу
POST /api/tasks - создать задачу
PUT /api/tasks/{id} - отредактировать существующую задачу
DELETE /api/tasks/{id} - удалить одну задачу



Поддерживает пагинацию (настройки в settings.py, установлена на 5)
Сортировка по всем полям, например:
http://127.0.0.1:8000/api/tasks/?ordering=-timestamp_create

Так же фильтр по полям text, is_done, пример:
http://127.0.0.1:8000/api/tasks/?text=3&is_done=true

Названия полей в модели text, is_done, timestamp_create, timestamp_done.