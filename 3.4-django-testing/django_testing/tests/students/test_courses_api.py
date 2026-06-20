import pytest
from model_bakery import baker
from students.models import Student, Course
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/1/')

    data = response.json()

    assert courses[0].id == data['id']
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    data = response.json()

    assert len(courses) == len(data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?id={courses[1].id}')

    data = response.json()

    assert courses[1].id == data[0]['id']
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/?name={courses[5].name}')

    data = response.json()

    assert courses[5].name == data[0]['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_course(client):
    course = {
        'name': 'Course_test'
    }

    response = client.post(f'/api/v1/courses/', data=course)

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)

    course = {
        'name': 'Course_test'
    }

    response = client.put(f'/api/v1/courses/{courses[3].id}/', data=course)

    data = response.json()

    assert course['name'] == data['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.delete(f'/api/v1/courses/{courses[3].id}/')

    assert response.status_code == 204