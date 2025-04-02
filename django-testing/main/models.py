from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    """
    Task model
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}: {self.due_date}"
