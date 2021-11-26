from django.db import models


# Create your models here.
from users.models import Users


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rep_url = models.URLField(max_length=256, blank=True)
    users = models.ManyToManyField(Users)


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
