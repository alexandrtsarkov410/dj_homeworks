# Действуем по аналогии с 18 слайдом презентации, используем команды.

docker build -t my_nginx /указываем путь к Dockerfile/

docker run --name my_nginx-server -d -p 8080:80 my_nginx
