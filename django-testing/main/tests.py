import datetime
import zoneinfo

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

    def test_create_task(self) -> None:
        """
        Test creating a new Task.
        :return:
        """
        form = TaskForm(data={'title': 'Test Task', 'due_date': '2026-03-03', 'description': 'Test description'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['title'], 'Test Task')
        self.assertEqual(form.cleaned_data['description'], 'Test description')
        self.assertEqual(form.cleaned_data['due_date'],
                         datetime.datetime(2026, 3, 3, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')))

    def test_create_task_with_empty_required_fields(self) -> None:
        """
        Test creating a new Task with empty required fields.
        :return:
        """
        form = TaskForm(data={'due_date': '', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.as_data()['title'])
        self.assertTrue(form.errors.as_data()['due_date'])

    def test_create_task_with_not_valid_date(self) -> None:
        """
        Test creating a new Task with invalid date.
        :return:
        """
        form = TaskForm(data={'title': 'Test Task', 'due_date': '2012-03-03', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.as_data()['due_date'])
        self.assertEqual(form.errors.as_data()['due_date'][0], forms.ValidationError('Due date must be in the future'))


@pytest.mark.django_db
@pytest.mark.parametrize("serializer_data, expected_field_error", [
    ({'title': '', 'description': 'Test description', 'due_date': '2026-03-03'}, 'title'),
    ({'title': 'Test Task', 'description': 'Test description', 'due_date': '2012-03-03'}, 'due_date'),
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
def test_create_task_with_valid_data() -> None:
    """
    Test creating a new Task with valid data.
    :return:
    """
    serializer = TaskSerializer(
        data={'title': 'Test Task', 'description': 'Test description', 'due_date': '2026-03-03'})
    assert serializer.is_valid()
    task = serializer.save()
    assert task.title == 'Test Task'
    assert task.description == 'Test description'
    assert task.due_date == datetime.datetime(2026, 3, 3, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
