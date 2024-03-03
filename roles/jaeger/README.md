MONITORING
==================
Роль для создания и деплоя прометеус кластера.

Переменные
----------

* `elastic_stack_name`: Название стэка(По-умолчанию: elastic).

Использование
-------------

```yaml
- name: 'Деплой elasticsearch'
  include_role:
    name: 'elastic_swarm'
  vars:
    elastic_stack_name: elastic
```