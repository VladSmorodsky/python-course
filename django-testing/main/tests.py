import datetime
import zoneinfo

from django.contrib.auth.models import User
from django.test import TestCase
from django import forms
import pytest

from main.forms import TaskForm
from main.serializers import TaskSerializer


# Create your tests here.

class TaskCreationFormTestCase(TestCase):
    """
    Test case for Task creation form.
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test11', password='testP@$$w0rd', email='test11@example.com')

    def test_create_task(self) -> None:
        """
        Test creating a new Task.
        :return:
        """
        form = TaskForm(data={'title': 'Test Task', 'due_date': '2026-03-03', 'description': 'Test description',
                              'user': self.user})
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(form.cleaned_data['title'], 'Test Task')
        self.assertEqual(form.cleaned_data['description'], 'Test description')
        self.assertEqual(form.cleaned_data['due_date'],
                         datetime.datetime(2026, 3, 3, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')))

    def test_create_task_with_empty_required_fields(self) -> None:
        """
        Test creating a new Task with empty required fields.
        :return:
        """
        form = TaskForm(data={'due_date': '', 'description': '', 'user': self.user})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.as_data()['title'])
        self.assertTrue(form.errors.as_data()['due_date'])

    def test_create_task_with_not_valid_date(self) -> None:
        """
        Test creating a new Task with invalid date.
        :return:
        """
        form = TaskForm(data={'title': 'Test Task', 'due_date': '2012-03-03', 'description': '', 'user': self.user})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.as_data()['due_date'])
        self.assertEqual(form.errors.as_data()['due_date'][0], forms.ValidationError('Due date must be in the future'))


@pytest.fixture
def user_fixture(db):
    return User.objects.create_user(username='test', password='testP@$$w0rd', email='test@example.com')


@pytest.mark.django_db
@pytest.mark.parametrize("serializer_data, expected_field_error", [
    ({'title': '', 'description': 'Test description', 'due_date': '2026-03-03'}, 'title'),
    ({'title': 'Test Task', 'description': 'Test description', 'due_date': '2012-03-03'},
     'due_date'),
])
def test_invalid_serializer(serializer_data, expected_field_error) -> None:
    """
    Test
    :return:
    """
    serializer = TaskSerializer(data=serializer_data)
    assert not serializer.is_valid()
    assert expected_field_error in serializer.errors


@pytest.mark.django_db
def test_create_task_with_valid_data(user_fixture) -> None:
    """
    Test creating a new Task with valid data.
    :return:
    """
    user = User.objects.create_user(username='test11', password='testP@$$w0rd', email='test11@example.com')
    data = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'due_date': '2026-03-03',
        'user': user.id
    }
    serializer = TaskSerializer(data=data)
    assert serializer.is_valid()
    task = serializer.save()
    task.refresh_from_db()
    assert task.title == 'Test Task'
    assert task.description == 'This is a test task'
    assert task.due_date == datetime.datetime(2026, 3, 3, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
    assert task.user == user


@pytest.mark.django_db
def test_create_task_with_not_existed_user(user_fixture) -> None:
    """
    Test creating a new Task with not existed user in database.
    :param user_fixture:
    :return:
    """
    user = User(username='test11333', password='testP@$$w0rd',
                email='test113333@example.com')  # user is not exists in db
    data = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'due_date': '2026-03-03',
        'user': user.id
    }
    serializer = TaskSerializer(data=data)
    assert not serializer.is_valid()
    assert serializer.errors['user']
