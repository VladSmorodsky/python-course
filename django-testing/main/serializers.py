from rest_framework import serializers

from main.models import Task
from main.validators import validate_title, validate_due_date


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model
    """
    title = serializers.CharField(validators=[validate_title])
    due_date = serializers.DateTimeField(validators=[validate_due_date])

    class Meta:
        model = Task
        fields = '__all__'
