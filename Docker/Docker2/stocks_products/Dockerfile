FROM python:latest
WORKDIR /django_task_CRUD
COPY requirements.txt /django_task_CRUD/
COPY  . /django_task_CRUD.
RUN pip install -r requirements.txt
#RUN python manage.py makemigrations
#RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]