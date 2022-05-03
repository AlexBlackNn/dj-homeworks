# https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni
# in case of "Got an error creating the test database: permission denied to
# create database"

"""When Django runs the test suite, it creates a new database, in your case
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


# Фабрика курсов
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


# Фабрика студентов
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_one_course(client, student_factory, course_factory):
    """Проверка получения 1го курса (retrieve-логика)."""
    # Arrange stage
    # Определяем количество курсов в начале
    num_courses = Course.objects.count()
    # создаем курс через фабрику
    course = course_factory(_quantity=1)
    # создаем студента через фабрику
    student = student_factory(_quantity=1)
    # добавляем студента к курсу
    course[0].students.add(student[0])
    # Act stage
    # Делаем запрос к endpoint
    response = client.get(f'/api/v1/courses/{course[0].id}/')

    # Assert stage
    # проверка, что запрос прошел удачно
    assert response.status_code == status.HTTP_200_OK

    # проверка, что число курсов увеличилось на 1 после его создания
    assert num_courses + 1 == Course.objects.count()

    # проверяем, что вернулся именно тот курс, который запрашивали
    data = response.json()
    assert data.get('name') == course[0].name


@pytest.mark.django_db
def test_get_course_filters_name(client, student_factory, course_factory):
    """Фильтрация по name."""
    # Arrange stage
    # Определяем количество курсов в начале
    num_courses = Course.objects.count()
    # создаем курс через фабрику
    course = course_factory(_quantity=1)

    # создаем студента через фабрику
    student = student_factory(_quantity=1)
    # добавляем студента к курсу
    course[0].students.add(student[0])

    # Act stage
    # Делаем запрос к endpoint
    response = client.get(f'/api/v1/courses/?name={course[0].name}')

    # Assert stage
    # проверка, что запрос прошел удачно
    assert response.status_code == status.HTTP_200_OK

    # проверка, что число курсов увеличилось на 1 после его создания
    assert num_courses + 1 == Course.objects.count()

    # проверяем, что вернулся именно тот курс, который запрашивали
    data = response.json()
    assert data[0].get('name') == course[0].name

@pytest.mark.django_db
def test_get_course_filters_id(client, student_factory, course_factory):
    """Фильтрация по id."""
    # Arrange stage
    # Определяем количество курсов в начале
    num_courses = Course.objects.count()
    # создаем курс через фабрику
    course = course_factory(_quantity=1)

    # создаем студента через фабрику
    student = student_factory(_quantity=1)
    # добавляем студента к курсу
    course[0].students.add(student[0])

    # Act stage
    # Делаем запрос к endpoint
    response = client.get(f'/api/v1/courses/?id={course[0].id}')

    # Assert stage
    # проверка, что запрос прошел удачно
    assert response.status_code == status.HTTP_200_OK

    # проверка, что число курсов увеличилось на 1 после его создания
    assert num_courses + 1 == Course.objects.count()

    # проверяем, что вернулся именно тот курс, который запрашивали
    data = response.json()
    assert data[0].get('name') == course[0].name

@pytest.mark.django_db
def test_get_list_courses(client, student_factory, course_factory):
    """Проверка получения списка курсов (list-логика)."""
    # Arrange stage
    # Определяем количество курсов в начале
    quantity = 5
    num_courses = Course.objects.count()
    # создаем курс через фабрику
    courses = course_factory(_quantity=quantity)
    # создаем студента через фабрику
    students = student_factory(_quantity=quantity)
    # добавляем студента к курсу
    for course, student in zip(courses, students):
        course.students.add(student)

    # Act stage
    # Делаем запрос к endpoint
    response = client.get('/api/v1/courses/')

    # Assert stage
    # проверка, что запрос прошел удачно
    assert response.status_code == status.HTTP_200_OK

    # проверка, что число курсов увеличилось на 1 после его создания
    assert num_courses + quantity == Course.objects.count()

    # проверяем, что вернулся именно тe курсы, которые запрашивали
    data = response.json()
    for course, dict_ in zip(courses, data):
        assert dict_.get('name') == course.name


@pytest.mark.django_db
def test_get_course_with_id(client, student_factory, course_factory):
    """Проверка фильтрации списка курсов по id."""
    # Arrange stage
    # Определяем количество курсов в начале
    quantity = 5
    # создаем курс через фабрику
    courses = course_factory(_quantity=5)
    # создаем студента через фабрику
    students = student_factory(_quantity=quantity)
    # добавляем студента к курсу
    for course, student in zip(courses, students):
        course.students.add(student)
    # Act stage
    # Делаем запрос к endpoint
    response = client.get(f'/api/v1/courses/{courses[-1].id}/')

    # Assert stage
    # проверка, что запрос прошел удачно
    assert response.status_code == status.HTTP_200_OK

    # проверяем, что вернулся именно тот курс, который запрашивали
    data = response.json()
    assert data.get('name') == courses[-1].name




@pytest.mark.django_db
def test_create_course(client, student):
    """Тест успешного создания курса."""
    # создаем студента
    #  в client.post в students передается id студента
    courses_at_start = Course.objects.count()
    response = client.post('/api/v1/courses/', data={
                    'name': 'django',
                    'students': student.id
                }
                )
    courses_in_the_end = Course.objects.count()
    assert response.status_code == status.HTTP_201_CREATED
    assert courses_at_start+1 == courses_in_the_end


@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    """Тест обновления курса."""
    # создаем студента
    #  в client.post в students передается id студента
    # создаем курс через фабрику
    course = course_factory(_quantity=1)
    # создаем студента через фабрику
    student = student_factory(_quantity=1)
    # добавляем студента к курсу
    course[0].students.add(student[0])

    courses_at_start = Course.objects.count()
    response = client.patch(f'/api/v1/courses/{course[0].id}/', data={
                    'name': 'django_v2',
                }
                )
    courses_in_the_end = Course.objects.count()
    assert response.status_code == status.HTTP_200_OK
    assert courses_at_start == courses_in_the_end

    # проверка обновления
    data = response.json()
    assert data.get('name') == 'django_v2'

@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    """Тест успешного удаления курса."""
    # создаем студента
    #  в client.post в students передается id студента
    # создаем курс через фабрику
    course = course_factory(_quantity=1)
    # создаем студента через фабрику
    student = student_factory(_quantity=1)
    # добавляем студента к курсу
    course[0].students.add(student[0])

    courses_at_start = Course.objects.count()
    response = client.delete(f'/api/v1/courses/{course[0].id}/')
    print(response.status_code)
    courses_in_the_end = Course.objects.count()
    print(courses_in_the_end)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert courses_at_start-1 == courses_in_the_end
