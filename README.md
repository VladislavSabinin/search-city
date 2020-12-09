# search-city

### TODO
1. Скачать файл.
1. Разархивировать.
1. Создать файл БД (SQLite).
1. Создать таблицу places (id - bigint8, geoname_id - varchar(10), eng_name - varchar(200), latitude - numeric(8,5), longitude - numeric(8,5), population - bigint8, created - TIMESTAMP, updated - TIMESTAMP, version - int4). Использовать дэфолтные значения дял некоторых полей (что и как в гугл, для каких - самому подумать).
1. Читать разархивированный файл, построчно! И записывать в БД 
1. Удалить лишние файлы.
