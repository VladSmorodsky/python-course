from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def __repr__(self):
        """
        :returns customer model representation
        :return:
        """
        return "<Customer {}>".format(self.username)

