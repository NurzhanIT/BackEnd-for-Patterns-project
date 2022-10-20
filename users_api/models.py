from django.db import models


# Create your models here.
class User(models.Model):
    nick = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    avatar = models.URLField(max_length=300)

    def __str__(self):
        return self.first_name
