# Описание и установка

### Добавил еще один способ обновления
Поскольку pandas более привычен, но, как говорят (и это так) память кушает,
сделал еще и через COPY.
Посмотрел профайлером скрипт с pandas использует 350Mb (и от размера файлов зависит), c COPY 131 Mb.
Точнее потребляемая pandas память зависит от самого большого файла, насколько я могу судить по профайлеру. Т.е. если добавятся остальные сегменты данных примерно такими же кусками, pandas больше потреблять не станет.

Выбор пандас изначально обусловлен реальной задачей, данными и затраченным временем, а не сферическими конями в безвоздушном пространстве.
Выгрузка данных и нормализация с pandas заняла минут 30-40, с sql 2 часа: подзабыл, а кое что и не использовал никогда.
Ну и валидация с pandas проще делается.

### Можно запустить в docker

В папке docker

Только при первом запуске выполнить команду (поскольку два контейнера на одном образе, билдим его первым).

>
    docker compose build --no-cache back

Затем как всегда
>
    docker compose up

Какое-то время скачивание файлов займет. В папке files должны появиться.
Кода стартанет, проверять по адресам
>
    localhost:8001
    localhost:8001/admin/
    localhost:8001/api/schema/swagger-ui/#/

admin user: atrucks/atrucks 
Info доступно только при авторизации в админе

Немного не так как хотел сделал докер, этот только для демонстрации (в некоторых местах не очень правильно сделано), хотелось полноценно инициализацию базы, создание пользователя и первоначальную загрузку сделать.

#### Зависимости
redis, uv, python3.12, yarn, node==22, postgres - вроде все

#### Запуск

##### back, в папке backend 
> 
    uv sync
    uv run src/manage.py runserver 9200

##### celery, в папке backend/src
> 
    celery -A core worker -B --loglevel=INFO

##### front, в папке frontend
>
    yarn
    vite

##### база
- Создаем базу atruck_swk, и пользователя. У меня настроен пользователь для соединения с БД (atruck_swk)  django/123, в файле backend/src/core/settings/local.py. Но на всякий случай я базу положил
- в папке backend/src 
>
    uv run manage.py migrate

И еще надо для тестов базу, обычно я делаю с префиксом test_. Но для тестов я только настройки сделал.

##### команды
>
    uv run manage.py create_admin  # - делает юзера 	atrucks/atrucks
    uv run manage.py force_update  # - если у вас все стартануло, то дергает задачу celery, на скачивание и обработку файлов. (возможно надо будет создать паку files в корне проекта).



##### urls
>
    localhost:9200/admin/
    localhost:3200/
    localhost:9200/api/schema/swagger-ui/#/




# Список задач и затраченное время

- [x] <span class="timer-btn" timerId="1765297219483" Status="Paused" AccumulatedTime="1495" currentStartTimeStamp="null" lineId="2" >【⏳00:24:55 】 </span>django create env, admin
- [x] <span class="timer-btn" timerId="1765299362808" Status="Paused" AccumulatedTime="959" currentStartTimeStamp="null" lineId="3" >【⏳00:15:59 】</span> init models
- [x] <span class="timer-btn" timerId="1765301203139" Status="Paused" AccumulatedTime="9425" currentStartTimeStamp="null" lineId="4" >【⏳02:37:05 】 </span>add celery task for download and process files, work on models, logs
- [x] <span class="timer-btn" timerId="1765363984844" Status="Paused" AccumulatedTime="2383" currentStartTimeStamp="null" lineId="4" >【⏳00:39:43 】 </span>add  api view
- [ ] <span class="timer-btn" timerId="1765349283762" Status="Paused" AccumulatedTime="666" currentStartTimeStamp="null" lineId="7" >【⏳00:11:06 】 </span>make test env backend, and tests (окружение сделал)
- [x] <span class="timer-btn" timerId="1765370974722" Status="Paused" AccumulatedTime="2488" currentStartTimeStamp="null" lineId="6" >【⏳00:41:28 】 </span>нормализация базы при вставке данных (регион специально убрал, он вроде как дублируется) (но именно для этой задачи я возможно бы и не делал, данные не наши, мы их не поддерживаем, а всякие парсеры и обработки проще. Единственно добавил бы числовые поля для диапазона номеров как PhoneNorm )
- [ ] Можно еще поле name в модели территория разбить на два (там | ) и тоже нормализовать, но если только по номеру искать то не обязательно
- [ ] заменить requests на selenium (защита по user-agent уже есть, еще что-то могут добавить.)
- [ ] проверка на необходимость обновлять данные в БД минут 30-40 заняло бы (наверно md5 проверять, но на этой задаче не особо важно, быстро же проверяется по базе с execute_values)
- [x] <span class="timer-btn" timerId="1765431085450" Status="Paused" AccumulatedTime="1008" currentStartTimeStamp="null" lineId="10" >【⏳00:16:48 】 </span>посмотреть как будет работать партицирование таблицы (работает, но разница небольшая на этих данных)
- [x] <span class="timer-btn" timerId="1765381720719" Status="Paused" AccumulatedTime="6721" currentStartTimeStamp="null" lineId="11" >【⏳01:52:01 】 </span>create frontend
- [ ] Makefile
- [x] pack into docker
- [ ] readme
- [ ] frontend tests
- [ ] по хорошему парсер надо. там на ссылке похоже timestamp (но от 24-го года), можно проверять надо ли скачивать файлы(если он настоящий).
