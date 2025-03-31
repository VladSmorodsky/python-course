from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Task
from main.validators import validate_title, validate_due_date


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model without user relation
    """
    title = serializers.CharField(validators=[validate_title])
    due_date = serializers.DateTimeField(validators=[validate_due_date])
    description = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'due_date', 'description', 'user']

    def validate_id(self, value: int) -> int:
        """
        Validate if user with id exists
        :param value:
        :return:
        """
        user = User.objects.filter(pk=value).first()
        if not user:
            raise serializers.ValidationError("User does not exist")
        return value

    def validate_username(self, value: str) -> str:
        """
        Validate that user with given username exists
        :param value:
        :return:
        """
        user = User.objects.filter(username=value).first()
        if not user:
            raise serializers.ValidationError('User does not exist')
        return value

    def validate_email(self, value: str) -> str:
        """
        Validate that user with given email exists
        :param value:
        :return:
        """
        user = User.objects.filter(email=value).first()
        if not user:
            raise serializers.ValidationError('User does not exist')
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
