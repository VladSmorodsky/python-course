import datetime
import zoneinfo

from django.test import TestCase
from django import forms

from main.forms import TaskForm


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
