CHECK_STACK_STATUS
==================
Роль для ожидания деплоя сварм стэка. Фейлится если сервисы не получают статус Running.

Зависимости
-----------

watch

ansible-galaxy install -p roles -r requirements.yml -f

Переменные
----------

* `wait_sh_path_install`: Путь куда будет скопирован шелл скрипт ожидающий деплой стэка. (default=/opt)
* `stack_name`: Имя стэка для ожидания.
