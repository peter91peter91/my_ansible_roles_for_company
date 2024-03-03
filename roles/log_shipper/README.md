LOG_SHIPPER
==================
Сбор логов через Promtail\Vector с нод Docker Swarm.
Promtail\Vector разворачивается в отдельный контейнер и через docker socket получает логи с Docker.
Не использует драйвер docker loki plugin.

Для лейбла container_node используется проброс hostname ноды.
Для лейбла container_service используется проброс вшитого в docker swarm лейбла.

Логика работы
----------

1. При включении данной роли в плейбук самое главное указать хосты на которых она должна быть развернута.
2. Происходит сканирование хостов на наличии docker swarm manager. А так же подсчет нод в кластере. 
3. Разворачивается по одному контейнеру на каждую ноду в кластере через ноды с docker swarm manager.
4. После этого Promtail\Vector в контейнере начинает собирать логи с docker socket на каждой ноде и посылать в Loki.

Переменные
----------

* `deploy_promtail`: Развернуть Promtail шиппер (По-умолчанию: false).
* `deploy_vector`: Развернуть Vector шиппер (По-умолчанию: false).
* `loki_host`: Адрес хоста с Loki (По-умолчанию: 10.10.11.170:3100).

Использование
-------------

```yaml
- name: 'Деплой Log Shipper'
  include_role:
    name: 'log_shipper'
  vars:
    deploy_vector: true
    loki_host: "10.10.11.170:3100"
```