# Django Tree Menu
Тестовое задание

Это проект Django-приложения, которое реализует древовидное меню с использованием PostgreSQL.

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/your-repo/django-tree-menu.git
   cd django-tree-menu
Создайте виртуальное окружение и активируйте его:

##
python -m venv myenv
source myenv/bin/activate  # Для Windows используйте `myenv\Scripts\activate`

## Установите зависимости:
pip install -r requirements.txt
## Настройте переменные окружения в файле .env:

env
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL='postgres://user:password@localhost:5432/mydatabase'
## Создайте и примените миграции:
python manage.py makemigrations
python manage.py migrate
## Запустите сервер разработки:
python manage.py runserver 
## Функциональность
Древовидное меню с неограниченной вложенностью.
Меню редактируется через стандартную админку Django.
Поддержка named URL.
Определение активного пункта меню на основе текущего URL.

## Использование
Для отображения меню на странице используйте тег шаблона:

html

{% draw_menu 'main_menu' %}
