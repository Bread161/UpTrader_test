Имеется следующее задание :

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.


Инструкция ориентирована на операционную систему windows и утилиту git bash. 
Для прочих инструментов используйте аналоги команд для вашего окружения.

Клонируйте репозиторий и перейдите в него в командной строке:
git clone https://github.com/Bread161/UpTrader_test.git
Установите и активируйте виртуальное окружение:
python -m venv venv
source venv/Scripts/activate
Установите зависимости из файла requirements.txt:
pip install -r requirements.txt
В папке с файлом manage.py выполните миграции:
python manage.py migrate
Создайте суперюзера, зайдите в админку:
python manage.py createsuperuser
В папке с файлом manage.py запустите сервер, выполнив команду:
python manage.py runserver
Перейдите в админку и добавьте несколько пунктов и подпунктов ваших меню
Открываем главную страницу и видим результат проделанной работ.
Здесь вы можете увидеть скриншоты выполненной работы:

![Снимок экрана 2025-04-28 190938](https://github.com/user-attachments/assets/f98d307a-c950-4d2a-b436-0af580e2aeb0)


![Снимок экрана 2025-04-28 190948](https://github.com/user-attachments/assets/048c8de9-f161-4273-8c14-6fcb1c305748)


![Снимок экрана 2025-04-28 191038](https://github.com/user-attachments/assets/5c802b27-37c0-4877-98fb-9619b7cf22e4)



если хотите быстро проверить работу, то можете вызвать команду в терминале "python manage.py shell" и  вставить данный текст "from menu.models import Menu, MenuItem

# Создаем меню
main_menu = Menu.objects.create(name='main_menu')

# Верхний уровень
home = MenuItem.objects.create(title='Главная', url='/', menu=main_menu, order=1)
about = MenuItem.objects.create(title='О нас', url='/about/', menu=main_menu, order=2)
services = MenuItem.objects.create(title='Услуги', url='/services/', menu=main_menu, order=3)
contacts = MenuItem.objects.create(title='Контакты', url='/contacts/', menu=main_menu, order=4)

# Второй уровень (подпункты для "Услуги")
service1 = MenuItem.objects.create(title='Разработка сайтов', url='/services/web/', menu=main_menu, parent=services, order=1)
service2 = MenuItem.objects.create(title='SEO оптимизация', url='/services/seo/', menu=main_menu, parent=services, order=2)

# Третий уровень (подпункты для "Разработка сайтов")
MenuItem.objects.create(title='Интернет-магазины', url='/services/web/shops/', menu=main_menu, parent=service1, order=1)
MenuItem.objects.create(title='Корпоративные сайты', url='/services/web/corporate/', menu=main_menu, parent=service1, order=2)

print(' Меню успешно создано!')
" 
