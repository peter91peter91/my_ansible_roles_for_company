DOCKER
==================
Роль для предварительной подготовки докера на стендах перед деплоем. Включает в себя:
 - установку докера
 - настройку докера
 - установка основных пакетов для корректной работы ансибла с докером
 - инициализация сварма

Переменные
----------

* `registry_host`: адрес докер регистри.
* `registry_login`: логин для атворизации в регистри.
* `registry_pass`: пароль от регистри.
* `docker_daemon_options`: настройки докера которые будут записаны в /etc/docker/daemon.json (переменная не обязательная)

Пример использования:
```yaml
- name: Docker prepare
  include_role:
    name: docker
  vars:
    docker_daemon_options:
      data-root: "/data/docker"
      ipv6: false
      log-driver: "json-file"
      log-opts:
        max-size: "10m"
        max-file: "5"
    registry_host: registry.example.com
    registry_login: some_login
    registry_pass: "{{ lookup('env', 'ENV_VAR_WITH_PASSWORD') }}"
```