# Лабораторная работа №4

Вполнил: Стрыгин Д.Д.\
группа: М8О-111М-23\
вариант: 5

## Задание

Должны выполняться следующие условия:
- Кеш должен быть реализован с помощью Redis;

- Записи в кеше должны иметь срок жизни;

- Необходимо реализовать шаблоны «сквозное чтение» и «сквозная запись»

- Необходимо провести сравнение время отклика и максимальной пропускной способности сервиса по запросу данных клиента (пользователя) с помощью утилиты wrk с использованием кеша и без него. Результат тестирования сохранить в репозитории в файле performance.md.

## Результаты

Разработанные сервисы хранятся по пути
```
api/*
```
К ним добавился контейнер для redis. При выполении запроса сервисы сначала ищут ответ в redis, а еси не находят, то запрос перенаправляетя в proxysql. В случае получения данных от proxysql, результаты кешируются в redis на 60 сек. При выполнении вставки, например в чат группы, кеш из редиса удаляется, так как он теперь не соответствует актуальной информации.

Результаты тетсов скорости wrk и выводы по ним лежат по пути
```
tests/performance.md
```

## Выводы
Redis - нереляционная бд прямо в оперативной памяти. Инструмент обеспечивает кеширование и обладает всем необходимым для этого функионалом. Пользоваться им крайне удобно.