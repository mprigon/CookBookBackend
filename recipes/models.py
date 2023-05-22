from django.db import models
from django.contrib.auth.models import User


class Dish(models.Model):
    title = models.CharField(max_length=64)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    summary = models.TextField(max_length=256)
    recipe = models.TextField(max_length=512)
    photo = models.ImageField(upload_to="static/")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'Recipe of {self.title} category {self.cat}: {self.summary[:128]}...'


class Category(models.Model):
    nameCat = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return self.nameCat
