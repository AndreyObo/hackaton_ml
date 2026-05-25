Структура проекта:

- transform.py подготовка данных к исследованию
- research_and_model.ipynb исследование данных и построение модели
- main.py api
- model_provider.py класс для управления моделью и трансформации данных для api
- utils.py pydantic модели

Инициализация проекта:

- python -m venv venv
- .\venv\Scripts\activate
- pip install -r requirements.txt
- .\start_windows.bat

После этого api будет доступно по адресу http://localhost/ а swagger по адресу http://localhost/docs

Кроме того, в корневом каталоге проекта должна присутствовать директория data, содержащая файлы ga_hits.csv и ga_sessions.csv.
