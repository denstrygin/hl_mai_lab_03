## Тест производительности с помощью wkr

```
(base) root@DESKTOP-1B5EV3F:/# wrk -t4 -c50 -d30s "http://localhost:8000/search_users/?first_name_mask=Te&last_name_mask=Us"
Running 30s test @ http://localhost:8000/search_users/?first_name_mask=Te&last_name_mask=Us
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   519.33ms  217.64ms   1.79s    72.58%
    Req/Sec    24.73     13.39    70.00     52.76%
  2762 requests in 30.05s, 1.14MB read
  Socket errors: connect 0, read 0, write 0, timeout 1
Requests/sec:     91.92
Transfer/sec:     38.78KB
(base) root@DESKTOP-1B5EV3F:/# wrk -t4 -c50 -d30s "http://localhost:8000/search_users/?first_name_mask=Te&last_name_mask=Us"
Running 30s test @ http://localhost:8000/search_users/?first_name_mask=Te&last_name_mask=Us
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   505.40ms  278.55ms   1.98s    78.50%
    Req/Sec    27.97     16.15    90.00     60.93%
  2916 requests in 30.08s, 1.20MB read
  Socket errors: connect 0, read 0, write 0, timeout 2
Requests/sec:     96.94
Transfer/sec:     40.90KB
```

## Переведу результаты в удобно читаемый вид

Тест с кешированием:

- Среднее время отклика: 519.33 мс
- Запросов в секунду: 24.73
- Всего запросов: 2762
- Запросов в секунду: 91.92
- Передача в секунду: 38.78 КБ

Тест без кеширования:
- Среднее время отклика: 505.40 мс
- Запросов в секунду: 27.97
- Всего запросов: 2916
- Запросов в секунду: 96.94
- Передача в секунду: 40.90 КБ

## Выводы:
Для сравнения и тестирввал на 10 записях user, что подходят по текущему шаблону, поэтому результаты с кешированием не сильно опережают обычные запросы. Но, когда записей в базе данных станет занчительно больше, результат с кешом покажет себя лучше.

## PS 
У меня слабый ноут, я могу сгенерировать разительно больше данных, но у меня начнутся фризы, поэтому пишу тест на малом объёме:(