# BTC---tracker
Трекер данных цены биткоина 

Source: https://old.coindesk.com/coindesk-api

Загрузка и визуализация данных
Цель:
1) Получение исторических данных из внешнего api в формате [День: значение]
2) Сохранение(кэширование) полученных данных
3) Визуализация данных в виде графика

Требования:
1) Необходимый промежуток данных должен задаваться аргументами командной строки ArgumentParser
2) При получении исторических данных можно запросить максимум N дней за раз, где N - конфигурируемое значение < 100
3) При повторном запуске данные должны браться из кеша в приоритете

Дополнительный функционал:
* Поиск первого валидного дня исторических данных
* Минимизация количества запрашиваемых данных у внешнего апи(опциональный ключ запуска)
* Минимизация количества запросов(опциональный ключ запуска)
