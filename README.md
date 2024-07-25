# Django Tree Menu

Это проект Django-приложения, которое реализует древовидное меню с использованием PostgreSQL.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/your-repo/django-tree-menu.git
   cd django-tree-menu
Создайте виртуальное окружение и активируйте его:

sh
Копировать код
python -m venv myenv
source myenv/bin/activate  # Для Windows используйте `myenv\Scripts\activate`
Установите зависимости:

sh
Копировать код
pip install -r requirements.txt
Настройте переменные окружения в файле .env:

env
Копировать код
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL='postgres://user:password@localhost:5432/mydatabase'
Создайте и примените миграции:

sh
Копировать код
python manage.py makemigrations
python manage.py migrate
Запустите сервер разработки:

sh
Копировать код
python manage.py runserver
Функциональность
Древовидное меню с неограниченной вложенностью.
Меню редактируется через стандартную админку Django.
Поддержка named URL.
Определение активного пункта меню на основе текущего URL.
Использование
Для отображения меню на странице используйте тег шаблона:

html
Копировать код
{% draw_menu 'main_menu' %}
Лицензия
Этот проект лицензирован под MIT License.