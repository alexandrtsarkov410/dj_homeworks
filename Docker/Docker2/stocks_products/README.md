# Действуем по аналогии с Заданием 1

## Создаем контейнер
docker build -t django_task_CRUD /указываем путь к Dockerfile/

## Запускаем контейнер
docker run --name my_django_task_CRUD_server -d -p 8080:80 django_task_CRUD
