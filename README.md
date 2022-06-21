# [Сайт "Куда сходить?"](https://agrajag.pythonanywhere.com)

Это проект __сайта-интерактивной карты__. Он предназначен для размещения на нём "_точек интереса_" - локаций для досуга. Посетители сайта смогут найти поблизости от себя места интересные для посещения.  

 Демонстрационный пример размещен по адресу [agrajag.pythonanywhere.com](https://agrajag.pythonanywhere.com). Наполнение сайта ведется через __интерфейс администрирования__ по адресу [agrajag.pythonanywhere.com/admin/](https://agrajag.pythonanywhere.com/admin/).

### Как добавить новую локацию

1. Войдите в систему введя логин и пароль:

2. Напротив пункта `Локации` нажмите кнопку `Добавить`

3. Заполните поля описания локации, в "полном описании" можно использовать форматирование. Долгота и широта места указываются в градусах.

4. Добавьте изображения локации. После добавления изображения можно сортировать путем перетаскивания мышкой.

5. Сохраните локацию

### Как редактировать локации

В списке локаций доступен поиск по наименованию локации - найдите нужную. Перейдите в искомый объект. Вы сможете изменить поля описания локации, изменить порядок картинок путем перемещения их мышкой. Ненужную картинку можно удалить кнопкой `DELETE`.

### Административное добавление локаций

Для администратора, имеющего доступ к консоли сервера, существует консольная команда для добавления локаций из json-файлов. Например:
```
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Антикафе%20Bizone.json
```
Файл с описанием локации должен иметь следующую структуру:
```
{
    "title": <Название локации>,
    "imgs": [
        <Cсылка на картинку>,
        ...
        <Cсылка на картинку>,
    ],
    "description_short": <Краткое описание локации>,
    "description_long": <Полное описание локации с HTML-форматированием>,
    "coordinates": {
        "lng": <Долгота в  градусах>,
        "lat": <Широта в градусах>
    }
}
```
Файлы с описаниями локаций для демо-сайта были получены по адресу https://github.com/devmanorg/where-to-go-places

## Техническая информация

### Установка проекта
Для работы проекта необходим установленный `python3`. Проект создан на фреймворке Django. 
1. Установите необходимые зависимости командой
```
pip install -r requirements.txt
```
2. Создайте файл `.env`. В нем будут расположены параметры фреймворка:
    - Обязательный параметр
        - `SECRET_KEY = 'secret_key'`  
        требуется для формирования криптографических подписей. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY)
        - `DATABASE_URL = sqlite:////home/user/project/db.sqlite3`   
        URL строки подключения к базе данных. [Подробнее в документации.](https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url)
    - Необязательные параметры (_в примере указаны значения по-умолчанию_)
        - `DEBUG = False`  
        отвечает за включение режима отладки. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DEBUG)
        - `ALLOWED_HOSTS = 'localhost', '127.0.0.1'`  
        список адресов и доменов, которые обслуживает сайт. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-ALLOWED_HOSTS)
        - `STATIC_URL = '/static/'`  
        URL для обращения к файлам статики. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATIC_URL)
        - `STATIC_ROOT = 'static/'`  
        путь к файлам статики. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATIC_ROOT)
        - `MEDIA_URL = '/media/'`  
        URL для обращения к загруженным на сайт файлам. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_URL)
        - `MEDIA_ROOT = 'media/'`  
        путь к загруженным на сайт файлам. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-MEDIA_ROOT)
        - `LANGUAGE_CODE = 'en-us'`  
        код языка. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-LANGUAGE_CODE)
        - `USE_I18N = True`  
        включает подсистему переводов. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_I18N)
        - `USE_TZ = True`  
        учитывать часовой пояс или нет. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-USE_TZ)
        - `TIME_ZONE = 'UTC'`  
        часовой пояс сайта. [Подробнее в документации.](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-TIME_ZONE)

3. Создайте базу данных
```
python3 manage.py migrate
```
4. Создайте учетную запись администратора
```
python3 manage.py createsuperuser
```
5. Для локального запуска выполните команду
```
python3 manage.py runserver
```
6. При успешном запуске в консоль выведется сообщение
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 21, 2022 - 20:25:17
Django version 3.2.13, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Сайт будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000). Интерфейс администрирования сайта по адресу [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).



## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
