# https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni
# in case of "Got an error creating the test database: permission denied to create database"
"""hen Django runs the test suite, it creates a new database, in your case
test_db.  The postgres user with username django does not have permission to
create a database, hence the error message. When you run migrate or syncdb,
Django does not try to create the finance database, so you don't get any
errors.

You can add the createdb permission to the django user by running the following
 command in the postgres shell as a superuser (hat tip to this stack
 overflow answer).

=> ALTER USER alex CREATEDB;
!!!! alex extracted from settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_django_testing',
        'USER': 'alex',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Note: The username used in the ALTER USER <username> CREATEDB;
command needs to match the database user in your Django settings files.
 In this case, the original poster, had the user as django the above answer."""

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from students.models import Student, Course
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    student = Student.objects.create(id=1, name='Alex')
    student.save()
    return student

# Фабрика объектов
@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, student, message_factory):
    # Arrange (предустановка данных, запись их в ДБ и т.д.)
    courses = message_factory(_quantity=5)

    course = Course(id=len(courses)+1, name='django')
    course.save()
    course.students.add(student)
    # Act (функционал теста)
    response = client.get('/api/v1/courses/')

    # Assert(проверка, что действие выполнено корректно)
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert len(data) == len(courses)+1

    assert data[-1].get('name') == 'django'

@pytest.mark.django_db
def test_create_course(client, student):
    # создаем студента
    #  в client.post в students передается id студента
    courses_at_start = Course.objects.count()
    response = client.post('/api/v1/courses/', data={
                    'id': 1,
                    'name': 'django',
                    'students': student.id
                }
                )
    courses_in_the_end = Course.objects.count()
    assert response.status_code == status.HTTP_201_CREATED
    assert courses_at_start+1 == courses_in_the_end
