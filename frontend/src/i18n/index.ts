type Translation = {
    [key: string]: string;
};

const resources: { [lang: string]: Translation } = {
    ru: {
        header_phone: 'Реестр российской системы и плана нумерации',
        search_phone: 'Поиск по номеру',
        downloaded_info: 'Информация о загруженных данных',
        file_name: 'Название файла',
        is_added: 'Данные обновлены',
        is_downloaded: 'Файл скачан',
        retry_count: 'Количество попыток',
        updated_at: 'Дата обновления',
        status_message: 'Последнее сообщение',
        prefix: 'Префикс',
        num_min: 'Начальный номер',
        num_max: 'Конечный номер',
        capacity: 'Номеров',
        operator: 'Оператор',
        inn: 'ИНН',
        territory:  'Регион (ГАР)',
        phone_not_found: 'Телефон не найден',

        clear: 'Очисить',
        search: 'Поиск',
        cancel: 'Отменить',
        close: 'Закрыть',
        confirm_header: 'Подтвердите действие',
        confirm_message: 'Вы уверены что хотите закрыть редактирование и не сохранять данные?',
        edit: 'Редактировать',
        go_to_page: 'Перейти на страницу',
        no: 'Нет',
        not_found: 'Не найдено',
        save: 'Сохранить',
        yes: 'Да',

        //start: поля

        //end: поля
    },
};

const lang = 'ru';
export const t = (key: string): string => resources[lang][key] || key;
