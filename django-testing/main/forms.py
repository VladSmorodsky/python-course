from django import forms

from main.models import Task
from main.validators import validate_title, validate_due_date


class TaskForm(forms.ModelForm):
    """
    Task form
    """
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title'}),
                            validators=[validate_title])
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task description'}), required=False)
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Due date'}),
        validators=[validate_due_date])

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'user')
