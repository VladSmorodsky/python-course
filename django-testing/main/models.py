from django.db import models


# Create your models here.
class Task(models.Model):
    """
    Task model
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
