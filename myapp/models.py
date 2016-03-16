from django.db import models

class Kind(models.Model):
    name = models.CharField('Name', max_length=255)

class Food(models.Model):
    kind = models.ForeignKey(Kind, verbose_name="品種")
    name = models.CharField('名前', max_length=255)
