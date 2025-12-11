# Список задач

- [x] <span class="timer-btn" timerId="1765297219483" Status="Paused" AccumulatedTime="1495" currentStartTimeStamp="null" lineId="2" >【⏳00:24:55 】 </span>django create env, admin
- [x] <span class="timer-btn" timerId="1765299362808" Status="Paused" AccumulatedTime="959" currentStartTimeStamp="null" lineId="3" >【⏳00:15:59 】</span> init models
- [x] <span class="timer-btn" timerId="1765301203139" Status="Paused" AccumulatedTime="9425" currentStartTimeStamp="null" lineId="4" >【⏳02:37:05 】 </span>add celery task for download and process files, work on models, logs
- [x] <span class="timer-btn" timerId="1765363984844" Status="Paused" AccumulatedTime="2383" currentStartTimeStamp="null" lineId="4" >【⏳00:39:43 】 </span>add  api view
- [ ] <span class="timer-btn" timerId="1765349283762" Status="Paused" AccumulatedTime="666" currentStartTimeStamp="null" lineId="7" >【⏳00:11:06 】 </span>make test env backend, and tests
- [x] <span class="timer-btn" timerId="1765370974722" Status="Paused" AccumulatedTime="2488" currentStartTimeStamp="null" lineId="6" >【⏳00:41:28 】 </span>нормализация базы при вставке данных (регион специально убрал, он вроде как дублируется) (но именно для этой задачи я возможно бы и не делал, данные не наши, мы их не поддерживаем, а всякие парсеры и обработки проще. Единственно добавил бы числовые поля для диапазона номеров как PhoneNorm )
- [ ] Можно еще поле name в модели территория разбить на два (там | ) и тоже нормализовать, но если только по номеру искать то не обязательно
- [ ] заменить requests на selenium (защита по user-agent есть, еще что-то могут добавить.)
- [ ] проверка на необходимость обновлять данные в БД минут 30-40 заняло бы (наверно md5 проверять, но на этой задаче не особо важно, быстро же проверяется по базе с execute_values)
- [x] <span class="timer-btn" timerId="1765431085450" Status="Paused" AccumulatedTime="1008" currentStartTimeStamp="null" lineId="10" >【⏳00:16:48 】 </span>посмотреть как будет работать партицирование таблицы (работает, но разница небольшая на этих данных)
- [x] <span class="timer-btn" timerId="1765381720719" Status="Paused" AccumulatedTime="6721" currentStartTimeStamp="null" lineId="11" >【⏳01:52:01 】 </span>create frontend
- [ ] Makefile
- [ ] pack into docker
- [ ] readme
- [ ] frontend tests
- [ ] по хорошему парсер надо. там на ссылке похоже timestamp (но от 24-го года), можно проверять надо ли скачивать файлы(если он настоящий).
