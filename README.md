## Для запуска нужен установить
### poetry
### python3.8

## Установите все зависимости
```
poetry install
```

## Войдите в вирт. окуржение
```
poetry shell
```


## Запуск kafka
```
docker-compose up -d
```

## Создать топик
```docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic fibonacci
```

## Читать сообщения 

```
docker exec --interactive --tty broker kafka-console-consumer --bootstrap-server broker:9092                        --topic fibonacci                        --from-beginning
```


## Запуск на python (записть)

```
python producer.py
```

## Запуск на python (чтение)

```
python consumer.py
```